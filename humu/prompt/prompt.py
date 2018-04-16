from __future__ import print_function

import csv
import os
import sys


class Prompt(object):
  """Command line prompt that stores the local inputs."""

  def __init__(self, data_path):
    super(Prompt, self).__init__()
    self.data_path = data_path
    self.companies = self._fetch_company_list()
    self.printable_companies = self._printable_companies_for_prompt()
    self.company_name = None

  def _fetch_company_list(self):
    os.chdir(os.path.join(self.data_path))

    return [dirname for dirname in os.listdir(os.getcwd())
                    if os.path.isdir(os.path.join(os.getcwd(), dirname))]

  def _printable_companies_for_prompt(self):
    printable_companies = []
    for index, name in enumerate(self.companies):
        printable_companies.append('{}) {}'.format(index+1, name))
    return printable_companies

  def _welcome_message(self):
    print('--------------------------------------------------------------')
    print('Welcome to the Humu Data Importer.')
    print('--------------------------------------------------------------\n')
    print('Please select the company you would like to import')

  def _company_selection_prompt(self):
    print(*self.printable_companies, sep='\n')

    try:
      company_number = input('Enter the company number: ')
      self.company_name = self.companies[company_number - 1]
    except IndexError, SyntaxError:
      print('\n')
      print('Company selected does not exist! Please type number again.')
      self._company_selection_prompt()
    except KeyboardInterrupt:
      sys.exit(1)
    except:
      print('\n')
      print('The company number was not entered correctly.  Please try again.')
      self._company_selection_prompt()

  def run(self):
    self._welcome_message()
    self._company_selection_prompt()
