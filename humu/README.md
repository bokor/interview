# Humu Interview: SWE Work Sample Org Zero Prompt

## Steps to setup and run the code
1. Unzip code package and cd into the project's root directory.  FYI the org_zero csv file is under data/org_zero directory.
2. Run chmod 755 configure_env.sh run_tests.sh
3. Run ./configure_env.sh
4. Run ./run_tests.sh
5. Run python runner.py
6. Select the company which to run the reports and terminal will display the
   output.
7. The JSON file representing the org chart will be written to output/org_chart.json.


## Task list
1. [DONE] The average tenure of all employees
2. [DONE] The minimum and maximum number of direct reports of Org Zero managers
3. [DONE] A JSON file representing the organizational hierarchy of Org Zero


## Lessons to think about
- Are there any questions would you ask to a customer who sent this data file?
  - What fields are required vs optional in their system
  - How should we handle malformed data
  - How should we handle missing information? Fail the whole file, record, or leave the data out?
  - Are all their CSV exports the same? Do they always have a header?
  - How do they deal with updates and how are they expressed in csv format? delta files, whole hog files?

- Did you make any assumptions while processing this data?
  - Assumed that manager employee id of #N/A was the top of the org chart (since there was no empty field and 1 only had 1 report)
  - Invalid or malformed data would be skipped
  - Displaying Report data via terminal would be sufficient.
  - Tenure is displayed in days, months and years.  Also assumed that tenure in months would be ok to calculate with 30 days as the demoninator.

- What will your future self in 6 months appreciate remembering?
  - CVS processing never gets easier :)
  - The architecture might change a bit along the way to support different files, formats, ingestion methods. As well as reports might take on different shapes(JSON, web, CSV, etc).
  - Invalid or malformed data could provide very inaccurate modeling results

- Anything else you’d like to share?
  - My personal reflection on this interview and work example can only be described as 100% positive and would love to talk about the experience in more details.

