# write a function to check if the year is leap or not

year = 1990

def is_leap(y):
    leap = False
    
    # Write your logic here
    if y%100 == 0 and y%400 != 0:
        leap = False
    elif y%4 == 0:
        leap = True
    
    return leap

print is_leap(year)