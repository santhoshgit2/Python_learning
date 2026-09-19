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
from http.cookiejar import user_domain_match

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


try:
    num1 = 10
    result = "Strongly typed" + num1
except Exception as err:
    print(f"General Exception caught -> {err}")
else:
    print("Executes if no exception occurred.")
finally:
    print("Always executes - closing connections.")


##Write a program that asks for an employee’s age.
##1. Checks its type is of string (think about using isinstance() function)
##2. Converts it to int (continue writing your program from here..)
##3. Prints the years pending for retirement, for eg. 60 is the retirement age.
age=input("Enter your Age")
print(isinstance(age,int))
age=int(age)
print("Your age is ",age)
ret=(60-age)
print("You have",ret,"years left to retire")


#Fix the type error in the following code for salary calculation:
salary = '50000'
salary=int(salary)
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus)

#13-09-2026
#A.Write a program that asks the user for:
#employee_name (string)
#base_salary (float)
#hra_percent (integer)
#bonus_amount (float)

#B.Convert inputs to the correct datatype if required.
#Calculate:
# HRA = base_salary * (hra_percent / 100)
# Total Salary = base_salary + HRA + bonus_amount
#C. Print the output like this:
#Employee: Arun
#Base Salary: 40000.0
#HRA @ 20%: 8000.0
#Bonus: 5000.0
#Total Salary Payable: ₹53000.0

empname:str=input("Enter your Name: ")
base_sal:float=input("Enter your Base Salary: ")
hra_per:int=input("Enter your Hra Percentage: ")
bonus:float=input("Enter your Bonus: ")

hra=float(base_sal)*float(hra_per)/100
tot_sal=float(base_sal) + hra + float(bonus)

print("Employee:",empname)
print("Base Salary:",float(base_sal))
print("Hra @",hra_per,"%", hra)
print("Bonus:",float(bonus))
print("Total Salary:",tot_sal)

print(list(empname,base_sal,hra,tot_sal))

#bugfix

item_name = input("Enter product name: ")
price = input("Enter price per item: ")
quantity = input("Enter quantity: ")
total_cost = float(price) * int(quantity)
print("You purchased " , quantity , " units of " , item_name)
print("Total payable: " , total_cost)


#17-09-2026

#Use Case 2: Student Result Classification
#a. Write a program that takes marks as input (initially as a string).
#B. Check if the value can be converted to float.
#C. Then classify (try using if condition with the help of AI, however we will learn about if condition soon):
#Marks >= 90 --> Outstanding
# Marks >= 75 --> Excellent
# Marks >= 50 --> Pass
# Marks < 50 --> Fail

mark=input("Enter mark: ")
mark=float(mark)
if mark >=90:
    print("Outstanding mark ",mark)
elif mark < 90 and mark >=75:
    print(f"Excellent mark {mark}")
elif mark < 75 and mark >=50:
    print("Pass mark ", mark)
else :
    print("Fail")


#H. Python Operators Usecases
#Use Case 1: Internet Data Usage Calculator
#Write a program that asks the user for:
#Total monthly data limit (in GB)
#Data used so far (in GB)
#Calculate using arithmetic operators:
# Remaining data = limit - used
# Usage percentage = (used / limit) * 100
#Print:
#Remaining data
#Usage percentage rounded to 2 decimals

tot_limit=input("Enter total limit in GB: ")
tot_limit=float(tot_limit)
used_data=input("Enter data to use in GB: ")
used_data=float(used_data)
bal_data =tot_limit - used_data
use_per= (used_data/tot_limit)*100
if use_per >= 80:
    print( "Remaining data:",bal_data)
    print(f"Warning: High usage : {use_per:.2f}, consider upgrading your plan.")
else:
    print("Remaining data:",bal_data)
    print(f"Usage percentage: {use_per:.2f}")


#Use Case 2: Shopping Discount Calculation
#Write a program that takes:
#Original price (float)
#Discount percent (int)
#Using assignment and arithmetic operators, calculate:
# Discount amount = (price * discount_percent) / 100
# Final price = price - discount_amount
#Print:
# Original price, discount applied, and final payable amount.

i_price=float(input("Enter price: "))
i_disc=int(input("Enter number of discount percent: "))
disc_amt=(i_price*i_disc)/100
fin_amt=i_price-disc_amt
print(f"Original price: {i_price}, discount applied: {disc_amt :.2f}, and final payable amount: {fin_amt:.2f}")

#Use Case 3 (Bug Fixing): Logical and Comparison Operator Errors
#The following code should determine voting eligibility, but it contains operator mistakes. Fix it.
#Incorrect code:
#age = input("Enter age: ")
# citizen = input("Are you an Indian citizen? (yes/no)")
#if age > "18" and citizen = "yes":
# print("Eligible to vote")
# else:
# print("Not eligible")
#Expected behavior:
#Convert age to integer before comparison.
#Only print "Eligible to vote" if age is 18 or above AND citizen input is "yes" (case-insensitive).

age = int(input("Enter age: "))
citizen = input("Are you an Indian citizen? (yes/no)")
citizen = citizen.lower()
if age > 18 and citizen == "yes":
    print("Eligible to vote")
else:
    print("Not eligible")


#I. Conditional Structure
#Use Case 1: Banking Eligibility Check
#Write a program that asks the user for:
##Age
#Monthly income
#Conditions:
##If age < 18: print "Not eligible for a bank account."
#If age >= 18 and income < 15000: print "Eligible for basic savings account."
#If age >= 18 and income between 15000 and 50000: print "Eligible for savings + salary account."
#If age >= 18 and income > 50000: print "Eligible for premium account."

age=int(input("Enter age: "))
income=float(input("Enter monthly income: "))
if age < 18:
    print("Not eligible for a bank account.")
elif age >= 18 and income < 15000:
    print("Eligible for basic savings account.")
elif age >= 18 and (income > 15000 or income < 50000):
    print("Eligible for savings + salary account.")
elif age >= 18 and income > 50000:
    print("Eligible for premium account.")

#another type:
age=int(input("Enter age: "))
income=float(input("Enter monthly income: "))
if age >=18:
    if income < 15000:
        print ("Eligible for basic savings account.")
    elif income > 15000 and income < 50000:
        print("Eligible for savings + salary account.")
    elif income > 50000:
        print("Eligible for premium account.")
else:
    print("Not eligible for a bank account.")


##Use Case 2: Check room availability
#-Check room availability
#    - If available:
#        - If guest is VIP
#            → Offer complimentary upgrade
#        - Else if member 5+ years
#            → Offer discount
#        - Else
#            → Standard price
#    - Else:
#        → Show: "No rooms available"

room_avail=int(input("Enter no of room availabe: "))
vip_ind=input("VIP customer Y or N: ")
mem_frm= int(input("Member from YYYY: "))
if room_avail > 0:
    if vip_ind == "Y" or vip_ind == "y":
        print("Offer complimentary upgrade")
    elif (2026-mem_frm) >= 5:
        print('Offer discount')
    else:
        print("Standard Price only")
else:
    print("No Rooms Available")


#Use Case 3 (Bug Fixing): Nested Condition Logic Issue
temp = input("Enter body temperature in Celsius: ")
temp = float(temp)
if temp < 37:
 print("Normal temperature")
elif temp > 37 and temp < 39:
 print("Fever")
else:
 print("High fever")


#Scenario 1
#Select the most suitable transportation option based on available money and ticket prices.

#Possible Options
#Flight
#Train
##Bus
#No transportation (because the budget is insufficient)

flight = 7000
train = 3000
bus = 2000
budget=float(input("Enter your Budget: "))
if budget >=2000:
    if budget >= flight:
        print("Flight is suitable for your Budget")
    elif budget < flight and budget >= train:
        print("Train is suitable for your Budget")
    else :
        print("Bus is suitable for your Budget")
else:
    print("No option is suitable for your Budget")
'''

#Scenario
#Apply a promotional discount to a food order.

#Business Rules
#Minimum cart value must be reached.
#Calculate the percentage discount.
#Compare the calculated discount with the maximum discount allowed.
#Apply whichever discount rule is appropriate.
#If the minimum cart value is not reached, tell the customer how much more needs to be added.

