"""1) Write a function `def to_underscore(string):` to move from CamelCase format to underscore format:
# saveChangesInTheEditor => save_changes_in_the_editor
# HelloHolbertonSchool => hello_holberton_school
"""


def to_underscore(string_in):
    string_out = ""
    for c in string_in:
        if c.isupper():
            string_out += "_" + c.lower()
        else:
            string_out += c
    return string_out

print "saveChangesInTheEditor => ",
print to_underscore("saveChangesInTheEditor")
print "HelloHolbertonSchool => ",
print to_underscore("HelloHolbertonSchool")