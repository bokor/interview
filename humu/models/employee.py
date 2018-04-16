class Employee(object):
  """Represents an Employee with could be a manager or not."""
  def __init__(self, employee_id,
               email_address=None, first_name=None, last_name=None,
               full_name=None, gender=None, start_date=None, is_manager=False,
               mgr_employee_id=None, level=None, title=None, location=None,
               department=None):
    super(Employee, self).__init__()
    self.employee_id = employee_id
    self.email_address = email_address
    self.first_name = first_name
    self.last_name = last_name
    self.full_name = full_name
    self.gender = gender
    self.start_date = start_date
    self.is_manager = is_manager
    self.mgr_employee_id = mgr_employee_id
    self.level = level
    self.title = title
    self.location = location
    self.department = department
