import unittest

from models.company import Company
from models.employee import Employee

class TestCompany(unittest.TestCase):

    def setUp(self):
      self.company = Company('Org Zero')

    def test_creation(self):
      self.assertEqual('Org Zero', self.company.name)

    def test_adding_employees(self):
      employee = Employee(101)
      self.company.add_employee(employee)
      self.assertEqual(employee, self.company.employees[101])
      self.assertEqual(1, len(self.company.employees))

    def test_adding_managers(self):
      employee = Employee(101, mgr_employee_id=2002)
      self.company.add_manager(employee)

      self.assertEqual(employee, self.company.managers[2002][0])
      self.assertEqual(1, len(self.company.managers))


if __name__ == '__main__':
    unittest.main()
