'''
teams = ['Data', 'AI', 'DevOps']
for t in teams:
  print('Hello', t, 'Team from Inceptez Technologies')
print('Keep Learning and Exploring!')
#####################################

students = 100
trainers = 2
total = students + trainers
print(total)


'''
print("Welcome to Inceptez Python Learning")
'''
word="""This is Inceptez's "Python" class for Data Engineers & AI Engineers
"""
print(word)

print ("""Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey.""")



sname='Santhosh'
course_nm='Python Fundamentals'
institute_nm='Inceptez Technologies'

print (sname,'is learning the',course_nm,'at the institute',institute_nm)


fee=45000
print ('Course fee=',fee)
fee=fee+(fee*.18)
print ('Course fee plus GST=',fee)

1) 2student = 'Ravi'  # Cannot start with number
2) _student_id = 1001 # Valid
3) studentName = 'Priya' #Valid
4) class name = 'Python' # cannot have spaces between
5) inceptez_batch = 'Morning' #valid



# Dictionary Switch Workaround
case_switch_using_dict = {
    0: "zero",
    1: "one",
    2: "two"
}

# Lookup pattern
result = case_switch_using_dict.get(0)
print(result)  # Output: "one"

'''
try:
    num1 = 10
    result = "Strongly typed" + num1
except Exception as err:
    print(f"General Exception caught -> {err}")
else:
    print("Executes if no exception occurred.")
finally:
    print("Always executes - closing connections.")