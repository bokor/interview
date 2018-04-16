import json
import os

from prompt.prompt import Prompt
from parser.csv_parser import CsvParser
from pprint import pprint
from report.report import Report

if __name__ == "__main__":
  data_path = os.path.join(os.getcwd(), 'data')
  output_path = os.path.join(os.getcwd(), 'output')

# 1) Set up and run the Command Line Prompt.
  prompt = Prompt(data_path)
  prompt.run()

# 2) After choosing the company name from the prompt, pass it along to the
# importer.
  csv_filepath = os.path.join(
    data_path, prompt.company_name, '{}.csv'.format(prompt.company_name))
  column_parser = CsvParser(prompt.company_name, csv_filepath)
  mgr_employee_ids = column_parser.collect_list_from_column(
    CsvParser.TYPE_INT, 'Manager Employee ID')
  start_dates = column_parser.collect_list_from_column(
    CsvParser.TYPE_STRING, 'Start Date')

# 3) Build & print report data.
  report = Report(prompt.company_name)

  # Build and print 'Max number of direct reports for manager'
  max_manager_id, max_total_report = report.total_direct_reports(
    Report.TYPE_DIRECT_REPORT_MAX, mgr_employee_ids)
  report.print_results_for_direct_reports(
    Report.TYPE_DIRECT_REPORT_MAX, max_manager_id, max_total_report)

  # Build and print 'Min number of direct reports for manager'
  min_manager_id, min_total_report = report.total_direct_reports(
    Report.TYPE_DIRECT_REPORT_MIN, mgr_employee_ids)
  report.print_results_for_direct_reports(
    Report.TYPE_DIRECT_REPORT_MIN, min_manager_id, min_total_report)

  # Build and print 'Avg. tenure of all employees'
  total_employees, avg_tenure_in_days = report.average_tenure_of_all_employees(
    start_dates)
  report.print_average_tenure_for_all_employees(
    total_employees, avg_tenure_in_days)

# 4) Export Org Chart in JSON.
  row_parser = CsvParser(prompt.company_name, csv_filepath)
  row_parser.parse()
  org_chart = row_parser.build_org_chart()
  row_parser.write_org_chart_as_json(org_chart, output_path)

  pprint(org_chart)
