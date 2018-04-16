import os
import unittest
import sys

from freezegun import freeze_time
from report.report import Report

# TODO(bokor): Move to a shared/common/helper library.
class SupressPrintStatements(unittest.TestCase):
  def setUp(self):
      f = open(os.devnull, 'w')
      sys.stdout = f

class TestTotalDirectReports(SupressPrintStatements):

    def setUp(self):
      f = open(os.devnull, 'w')
      sys.stdout = f

    def test_total_max_direct_reports(self):
      manager_id_list = [1,1,1,1,1,2,2,3,10,10,10]
      report = Report('Org Zero')

      manager_id, total_count = (
        report.total_direct_reports(
          Report.TYPE_DIRECT_REPORT_MAX, manager_id_list))
      self.assertEqual(1, manager_id)
      self.assertEqual(5, total_count)

    def test_total_min_direct_reports(self):
      manager_id_list = [1,1,1,1,1,2,2,3,10,10,10]
      report = Report('Org Zero')

      manager_id, total_count = (
        report.total_direct_reports(
          Report.TYPE_DIRECT_REPORT_MIN, manager_id_list))

      self.assertEqual(3, manager_id)
      self.assertEqual(1, total_count)

@freeze_time("2018-03-14")
class TestAverageTenureOfAllEmployees(SupressPrintStatements):

    def test_average_tenure_for_all_employees(self):
      start_dates = ['03/14/2002','01/14/2014','07/26/2000','01/12/2015',
                     '09/14/2015','12/01/2000','08/23/2004']
      report = Report('Org Zero')

      total_employees, avg_tenure_in_days = (
        report.average_tenure_of_all_employees(start_dates))

      self.assertEqual(7, total_employees)
      self.assertEqual(3876, avg_tenure_in_days)

if __name__ == '__main__':
    unittest.main(buffer=True)
