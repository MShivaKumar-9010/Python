#Comparison Operators (==, !=, >, <, >=, <=)

#Rahul scored 78 marks. The passing mark is 35.
 #Write a Python expression to check whether Rahul passed.
scoredmarks=78
passmarks=35
print(scoredmarks>=passmarks)


#Q2.
#A movie ticket is allowed only for people aged 18 or above.
 #A person's age is 16.
# Write an expression to check if they are eligible.
age=16
print(age>=18)


#A laptop costs ₹55,000.
 #Your budget is ₹60,000.
 #Check whether the laptop is within your budget.
laptop=55000
budget=60000
print(budget>=laptop)


#There are 25 students in Class A and 25 students in Class B.
# Write an expression to check whether both classes have the same number of students.
classA=25
classB=25
print(classA==classB)


#The temperature today is 42°C.
# Check whether the temperature is greater than 40°C.
temp=42
print(temp>=40)


#A customer entered the correct OTP 5678.
 #The entered OTP is 6789.
# Write an expression to check whether the OTP is incorrect.
correctOTP=5678
enteredOTP=6789
print(correctOTP==enteredOTP)

#The speed limit is 80 km/h.
# A car is moving at 80 km/h.
 #Check whether the car is following the speed limit.
speedlimit=80
movingcar=80
print(speedlimit==movingcar)


#A train has 150 seats.
 #Currently, 145 seats are booked.
# Check whether all seats are filled.
seats=150
booked_seats=145
print(seats==booked_seats)

#The minimum balance required in a bank account is ₹1000.
 #Current balance is ₹850.
# Check whether the balance is less than the required amount.
min_bal=1000
curr_bal=850
print(curr_bal<min_bal)


#A student needs at least 75% attendance.
 #Current attendance is 75%.
# Check whether the student is eligible for the exam.
min_att=75
curr_att=75
print(min_att==curr_att)


#Logical Operators (and, or, not)

#A student can attend the placement drive only if:
#CGPA is 7.5 or above
#Attendance is 75% or above
#Current CGPA = 8.1
#Attendance = 82%
curr_CGPA=8.1
att=82
print(curr_CGPA>=7.5 and att>=75)


#A customer gets free delivery if:Purchase amount is above ₹500Customer is a Prime member Purchase = ₹650Prime Member = TrueWrite the condition.
purs_amt=650
prime_no=True
print(purs_amt>=500 and prime_no is True)


#A website allows login if:
#Username is correct OR
#Email is correct
#Username Correct = False
#Email Correct = True
#Write the condition.
user_name=False
email_correct=True
print(user_name is True or email_correct is True)

#A cricket player is selected if:
#Runs > 500
#Wickets > 20
#Runs = 620
#Wickets = 18
#Write the condition.
runs=620
wickets=18
print(runs>500 and wickets>20)


#A student passes only if:
#Theory marks ≥ 35
#Practical marks ≥ 35
#Theory = 40
#Practical = 30
#Write the condition.
theory_marks=40
pract_marks=30
print(theory_marks>=35 and pract_marks>=35)

#A shop offers a discount if:
#Customer is a member
#OR total purchase exceeds ₹2000
#Member = False
#Purchase = ₹2500
#Write the condition.
mem=False
purs=2500
print(mem is True or purs>=2000)


#A person can vote if:
#Age is 18 or above
#AND is an Indian citizen
#Age = 20
#Citizen = True
#Write the condition.
age=20
citiz=True
print(age>=18 and citiz is True)


#A student is not absent.
#Absent = False
#Write a Python expression using the not operator to check whether the student is present.
absent=False
print(not(absent))

#A system grants admin access only if:Username is "admin" Password is correct Username = "admin" Password Correct = True Write the condition.
user_name="admin"
password_crt=True
print(user_name is "admin" and password_crt is True)


#A person can enter a swimming pool if:They have a membership OR they pay the entry fee Membership = False  Paid Fee = False 
Membership=False
entry_fee=False
print(Membership is True or entry_fee is True)


#Mixed Comparison + Logical Operators

#A student gets Grade A if: Marks are between 90 and 100 (inclusive).Marks = 95 Write the condition.
marks = 95
marks>90 and marks>100
print("grade-a")

#A customer is eligible for cashback if:Purchase ≥ ₹1000 AND purchase ≤ ₹5000 Purchase = ₹3200 Write the condition.
purs=3200
print(purs>=1000 and purs<=5000)


#A user can reset their password if:OTP is correct AND account is active OTP Correct = True Account Active = True Write the condition.
otp=True
acc_active=True
print(otp is True and acc_active is True)

#A player qualifies if:Age is between 18 and 25 (inclusive).Age = 23 Write the condition.
age=23
print(age>=18 and age<=24)


#A vehicle is fined if:Speed > 80 km/h OR signal is broken Speed = 75 Signal Broken = True Write the condition.
speed=75
signal_broken=True
print(speed>80 or signal_broken is False)


#Write a condition to check whether a number is between 10 and 50 (inclusive).
number=25
print(number>=10 and number<=50)


#Write a condition to check whether a person is either a student or a teacher.
name=input("student or teacher:")
print(name=="student" or name=="teacher")


#Write a condition to check whether a password length is at least 8 characters and contains at least one digit.
password=input("enter your password:")
print((len(password)>= 8)and (len(password)>=0))

#Write a condition to check whether a person's age is not less than 18.
print(age>=18)


#A customer gets a gift only if:Purchase amount is greater than ₹5000AND customer is a premium memberAND today is their birthdayWrite the condition using logical 
amount=6500
customer=True
birthday=True
print(bool(amount>5000 and customer==True and birthday==True))

