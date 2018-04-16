from collections import defaultdict

class Company(object):
  """Represents a Company with all employees and managers."""
  def __init__(self, name):
    super(Company, self).__init__()
    self.name = name
    self.employees = {}
    self.managers = defaultdict(list)

  def add_employee(self, employee):
    self.employees[employee.employee_id] = employee

  def add_manager(self, employee):
    self.managers[employee.mgr_employee_id].append(employee)
