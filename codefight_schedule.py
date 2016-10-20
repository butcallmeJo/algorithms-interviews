#from datetime 
import datetime

def rotate(l, n):
    return l[-n:] + l[:-n]

def recurring_task(firstDate, k, daysOfTheWeek, n):
    name_weekdays = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]
    first_day = datetime.datetime.strptime(firstDate, "%d/%m/%Y")
    # print name_weekdays[first_day.weekday()]

    # get first day out of the way
    outp = []
    # outp.append(first_day.strftime("%d/%m/%Y"))
    # n -= 1
    # if n <= 0:
    #     return outp
    # get rest of the week
    index = daysOfTheWeek.index(name_weekdays[first_day.weekday()])
    day_copy = first_day
    rot = rotate(daysOfTheWeek, index)
    while n >= 0:
        counter = 0
        day_copy2 = day_copy
        for item in rot:
            counter += 1
            # print counter, "item"
            # print n
            print day_copy
            outp.append(day_copy.strftime("%d/%m/%Y"))
            n -= 1
            if n <= 0:
                return outp
            xtra = name_weekdays.index(rot[index]) + day_copy.weekday()
            # print xtra
            day_copy += datetime.timedelta(days=(7-xtra))
            # print day_copy
            # print outp
        day_copy = day_copy2
        day_copy += datetime.timedelta(days=7*k)
        print day_copy, 3
        
        

    # while index < len(daysOfTheWeek)-1:
    #     if n <= 0:
    #         return outp
    #     index += 1
    #     n -= 1
    #     xtra = name_weekdays.index(daysOfTheWeek[index]) - day_copy.weekday()
    #     day_copy += datetime.timedelta(days=xtra)
    #     outp.append(day_copy.strftime("%d/%m/%Y"))

    # first new week
    # xtra = day_copy.weekday() - name_weekdays.index(daysOfTheWeek[0])
    # print xtra
    # day_copy += datetime.timedelta(days=7-xtra)
    # print day_copy.weekday()
    
    # repeat every k weeks   
    # while n > 0:
    #     xtra = day_copy.weekday() - name_weekdays.index(daysOfTheWeek[0])
    #     day_copy += datetime.timedelta(days=7*k-xtra)
    #     outp.append(day_copy.strftime("%d/%m/%Y"))
    #     n -= 1
    #     index = 0
    #     while index < len(daysOfTheWeek)-1:
    #         if n <= 0:
    #             return outp
    #         index += 1
    #         n -= 1
    #         xtra = name_weekdays.index(daysOfTheWeek[index]) - day_copy.weekday()
    #         day_copy += datetime.timedelta(days=xtra)
    #         outp.append(day_copy.strftime("%d/%m/%Y"))
        
    return outp

if __name__ == "__main__":
    recurring_task("01/01/2015", 2, ["Monday", "Thursday"], 4)
