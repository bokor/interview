import unittest

from models.employee import Employee

class TestEmployee(unittest.TestCase):

    def test_creation(self):
      employee = Employee(101, email_address='bokor@google.com',
        first_name='Brian', last_name='Bokor', full_name='Brian R Bokor',
        gender='Male', start_date='03/14/2016', is_manager=True,
        mgr_employee_id=202, level='27', title='Fellow...Hello',
        location='Mountain View', department='SWE')

      self.assertEqual(101, employee.employee_id)
      self.assertEqual('bokor@google.com', employee.email_address)
      self.assertEqual('Brian', employee.first_name)
      self.assertEqual('Bokor', employee.last_name)
      self.assertEqual('Brian R Bokor', employee.full_name)
      self.assertEqual('Male', employee.gender)
      self.assertEqual('03/14/2016', employee.start_date)
      self.assertTrue(employee.is_manager)
      self.assertEqual(202, employee.mgr_employee_id)
      self.assertEqual('27', employee.level)
      self.assertEqual('Fellow...Hello', employee.title)
      self.assertEqual('SWE', employee.department)
      self.assertEqual('Mountain View', employee.location)


if __name__ == '__main__':
    unittest.main()
