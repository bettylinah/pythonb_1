#we use def key word in function
# think of a function as a machine that takes an input and produces a result

def hello_func():
    print("i love compsci")

hello_func()

#benefit of functions
#i)allow as to reuse code without repeating ourselves
#EX
def hi_func():
    print("this is programming")# note that if we want to run the code more times we will have to print out more hi_func
hi_func()
hi_func()
hi_func()# note that we can also change the output by just changing at the print string or intergers


#USE OF RETURN
def staff():
   return "welcome to home page"
print(staff())

def staff_func(greeting,name):
    return '{},{}'.format(name,greeting)
print(staff_func("linah","hi"))

#args and kwargs
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info("maths","art",name='james',age =22)

#or
def people_info(*args,**kwargs):
    print(args)
    print(kwargs)
course=['maths','art']
info ={'name':'linah','age':24}
people_info(*course,**info)

#EXAMPLE QUIZ
#number of days per month,first value placeholder  for indexing purpose.
month_days =[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """Return True for leap years and False for non leap years."""
    return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)

def days_in_months(year,month):
    """Return number of days in that month in that year"""

    if not 1<=month <= 12 :
        return 'invalid month'

    if month ==2 and is_leap(year):
        return 29

    return month_days[month]
print(is_leap(2017))
print(days_in_months(2017,2))




