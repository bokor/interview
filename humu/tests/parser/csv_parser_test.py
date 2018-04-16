import os
import unittest
from parser.csv_parser import CsvParser


class TestCollectListFromColumn(unittest.TestCase):
    def setUp(self):
      self.csv_filepath = os.path.join(
        os.getcwd(), 'tests', 'data', 'test_data.csv')

    def test_collect_employee_ids(self):
      parser = CsvParser('Org Zero', self.csv_filepath)
      employee_ids = parser.collect_list_from_column(
        CsvParser.TYPE_INT, 'Employee ID')
      self.assertEqual(50, len(employee_ids))

    def test_collect_mgr_employee_ids(self):
      parser = CsvParser('Org Zero', self.csv_filepath)
      mgr_employee_ids = parser.collect_list_from_column(
        CsvParser.TYPE_INT, 'Manager Employee ID')
      self.assertEqual(48, len(mgr_employee_ids))

    def test_collect_start_dates(self):
      parser = CsvParser('Org Zero', self.csv_filepath)
      start_dates = parser.collect_list_from_column(
        CsvParser.TYPE_STRING, 'Start Date')
      self.assertEqual(50, len(start_dates))


if __name__ == '__main__':
    unittest.main()
