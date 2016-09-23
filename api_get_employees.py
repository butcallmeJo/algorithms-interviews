"""Assume there is a REST API available at "http://www.companyname.corp/api" for accessing employee information The employee information endpoint is "/employee/<id>" Each employee record you retrieve will be a JSON object with the following keys:
'name'  refers to a String that contains the employee's first and last name
'title' refers to a String that contains the employee's job title
'reports' refers to an Array of Strings containing the IDs of the employee's direct reports
Write a function that will take an employee ID and print out the entire hierarchy of employees under that employee.
For example, suppose that Flynn Mackie's employee id is 'A123456789' and his only direct reports are Wesley Thomas and Nina Chiswick. If you provide 'A123456789' as input to your function, you will see the sample output below.

 
-----------Begin Sample Output--------------
Flynn Mackie - Senior VP of Engineering
  Wesley Thomas - VP of Design
    Randall Cosmo - Director of Design
      Brenda Plager - Senior Designer
  Nina Chiswick - VP of Engineering
    Tommy Quinn - Director of Engineering
      Jake Farmer - Frontend Manager
        Liam Freeman - Junior Code Monkey
      Sheila Dunbar - Backend Manager
        Peter Young - Senior Code Cowboy
-----------End Sample Output--------------
"""

import requests

def print_employee_hierarchy(tab_size=0, id):
    # get info using requests
    # parse the info to get: name, title, reports
    # for every id in reports -> recurse print_emp_hierarchy(id)

    resp = requests.get("http://www.companyname.corp/api/employee/" + id)
    resp_json = resp.json()
    # resp_json.get("name")
    name = resp_json["name"]
    title = resp_json["title"]
    reports = resp_json["reports"]

    for _ in range(tab_size):
        print "\t",
        print "%s - %s" % (name, title)

    if not reports: 
        return

    tab_size += 1

    for id in reports:
        print_employee_hierarchy(tab_size, id)