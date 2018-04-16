import datetime
from dateutil import parser

class Report(object):
  """Creates different reporting options for data provided."""
  TYPE_DIRECT_REPORT_MAX = 'Max'
  TYPE_DIRECT_REPORT_MIN = 'Min'

  def __init__(self, company_name):
    super(Report, self).__init__()
    self.company_name = company_name

  def total_direct_reports(self, report_type, manager_id_list):
    counter = {}
    for manager_id in manager_id_list:
      if manager_id is None:
          continue

      if manager_id in counter:
        counter[manager_id] += 1
      else:
        counter[manager_id] = 1

    if report_type == Report.TYPE_DIRECT_REPORT_MAX:
      manager_id = max(counter, key=counter.get)
    elif report_type == Report.TYPE_DIRECT_REPORT_MIN:
      manager_id = min(counter, key=counter.get)
    else:
      raise TypeError('Incorrect report_type.')

    return (manager_id, counter[manager_id])

  def average_tenure_of_all_employees(self, start_dates):
    total_employees = 0
    total_tenure_in_days = 0

    today = datetime.date.today()
    for start_date in start_dates:
      try:
        formatted_date = parser.parse(start_date).date()
      except ValueError:
        continue

      if formatted_date > today:
        continue

      tenure = today - formatted_date
      total_employees += 1
      total_tenure_in_days += tenure.days

    avg_tenure_in_days = total_tenure_in_days / total_employees
    return (total_employees, avg_tenure_in_days)

  def print_results_for_direct_reports(self, report_type, manager_id, total):
    print('--------------------------------------------------------------')
    print('{} number of direct reports of {} managers'.format(
      report_type, self.company_name))
    print('--------------------------------------------------------------\n')
    print('Manager ID: {} '.format(manager_id))
    print('Direct Reports: {} '.format(total))
    print('\n')

  def print_average_tenure_for_all_employees(
    self, total_employees, avg_tenure_in_days):
    print('--------------------------------------------------------------')
    print('Avg. tenure for {} employees'.format(total_employees))
    print('--------------------------------------------------------------\n')
    print('Tenure in days: {} '.format(avg_tenure_in_days))
    print('Tenure in months: {} '.format(avg_tenure_in_days / 30))
    print('Tenure in years: {} '.format(avg_tenure_in_days / 365))
    print('\n')
