import csv
import json
import os

from models.company import Company
from models.employee import Employee


class CsvParser(object):
  """Import csv data files and create appropriate data models or aggregates."""
  TYPE_INT = 'int'
  TYPE_STRING = 'str'

  def __init__(self, company_name, csv_filepath):
    super(CsvParser, self).__init__()
    self.csv_filepath = csv_filepath
    self.company = Company(company_name)

  def parse(self):
    csv_file = open(self.csv_filepath)
    reader = csv.reader(csv_file)

    # TODO(bokor): Not the best solution and shoudl required a better mapping
    # layer to map header fields or data fields with object models.  This is
    # much easier to do with a webpage.
    reader.next() # Skips the header row

    for row in reader:
      employee = Employee(row[0], email_address=row[1], first_name=row[3],
        last_name=row[4], full_name=row[2], gender=row[10], start_date=row[9],
        is_manager=row[7], mgr_employee_id=row[12], level=row[5], title=row[6],
        location=row[8], department=row[11])
      self.company.add_employee(employee)
      self.company.add_manager(employee)

  def build_org_chart(self, org_chart=None, parent_manager_id='#N/A'): # 1 or # N/A
    employees = self.company.managers.get(parent_manager_id, None)
    if employees is None:
        return org_chart

    for employee in employees:
        direct_report = { 'id': employee.employee_id,
                          'email_address': employee.email_address,
                          'name': employee.full_name,
                          'level': employee.level,
                          'title': employee.title,
                          'gender': employee.gender,
                          'start_date': employee.start_date,
                          'is_manager': employee.is_manager,
                          'location': employee.location,
                          'department': employee.department }
        if org_chart is None:
            org_chart = direct_report
        else:
            reports = org_chart.setdefault('reports', [])
            reports.append(direct_report)
        self.build_org_chart(direct_report, employee.employee_id)
    return org_chart

  def write_org_chart_as_json(self, org_chart, output_path):
    json_filename = os.path.join(output_path, 'org_chart.json')
    with open(json_filename, 'w') as outfile:
      json.dump(org_chart, outfile)

    print('--------------------------------------------------------------')
    print(' JSON Org Chart:                                              ')
    print('--------------------------------------------------------------\n')
    print('Written to output file: {}'.format(json_filename))
    print('\n')

  def collect_list_from_column(self, column_type, column_name):
    csv_file = open(self.csv_filepath)
    dict_reader = csv.DictReader(csv_file)
    column_list = []
    for row in dict_reader:
      try:
        if column_type == CsvParser.TYPE_INT:
          column_value = int(row[column_name])
        elif column_type == CsvParser.TYPE_STRING:
          column_value = str(row[column_name])
        else:
          column_value = row[column_name]
        column_list.append(column_value)
      except ValueError:
        continue

    return column_list
