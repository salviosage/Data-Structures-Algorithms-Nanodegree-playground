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

###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day<30:
        return year,month,day+1
    else:
        if month<12:
            return year,month + 1,1
        else:
            return year + 1,1,1