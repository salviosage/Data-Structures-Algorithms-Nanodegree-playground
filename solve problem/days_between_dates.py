# pythonista's guide to all problems in the galaxy
# 0. dont panic 
# 1. whats are the inputs    = the birthday and current date simly two dates 
#   first date must be lower than the current date  
#   how are input presented    year,month,days
#2. what are the output  return number of day between dates 
#3. solve the problem
#  work out examples  define test scenarios 
# take next step   and keep finding simple solution, try out other methods 
#4. simple mechanical solutions 
# dont optimize prematurely, simple and correct 

# develop incrementaly and test as you go



# Credit goes to Websten from forums
#
# Program defensively:
#
# What do you do if your input is invalid? For example what should
# happen when date 1 is not before date 2?
#
# Add an assertion to the code for daysBetweenDates to give
# an assertion failure when the inputs are invalid. This should
# occur when the first date is not before the second date.
#  
def leapYear(year):
    if year % 400 ==0:
        return True 
    
    if year % 100 ==0:
        return False 
    if year % 4 ==0:
        return True
    return False
    
    

def daysInMonth(year,month):
    if month ==4 or month==6 or month==9 or month==11:
        return 30
    else:
        if month ==2:
            if leapYear(year):
                return 29
            return 28
    return 31

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    else:
        if month1 < month2:
            return True
        else: 
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    assert daysBetweenDates(2013,1,1,2013,1,1)== 0
    assert daysBetweenDates(2013,1,1,2013,1,2)== 1
    assert daysBetweenDates(2013,1,1,2014,1,1)== 365
    assert nextDay(2013,1,1)== (2013,1,2)
    assert nextDay(2013,4,30)== (2013,5,1)
    assert nextDay(2013,12,31)== (2014,1,1)
    assert nextDay(2013,2,28)== (2013,3,1)
    assert nextDay(2013,9,30)== (2013,10,1)
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result == answer and answer != "AssertionError":
                print ("Test case passed!")
            else:
                print ("Test with data:", args, "failed")
    
        except AssertionError:
            if answer == "AssertionError":
                print ("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print ("Check your work! Test case {0} should not raise AssertionError!\n".format(args))            
test()