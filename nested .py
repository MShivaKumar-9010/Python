# #Easy Level

# 1 Write a program to check whether a person is eligible to vote. If the person's age is 18 or above, check whether they have a voter ID. Print the appropriate message.
age=19
voter_id=True
if age>=18:
    if voter_id == True:
        print("eligible to vote")
    else:
        print("voter_id == false")
else:
    print("not eligible to vote")   
 
  

# 2 Write a program to check whether a student has passed. If the student scores 35 or more, check if the marks are 75 or above. Display "Distinction" or "Pass" accordingly.
marks=65
if marks>=35:
    if marks>=75:
        print("distinction")
    else:
        print("pass")
else:
    print("fail")


# 3 Write a program to check whether a user can log in.If the username is correct, check whether the password is correct.
username="shiva9010"
password=666666
if username == "shiva9010":
    if password == 666666:
        print("login successfull")
    else:
        print("incorrect password")
else:
    print("invalid username or password")


# 4 Write a program to check whether a person can drive. If the age is 18 or above, check whether they have a valid driving license.
age=21
driv_lic=True
if age>=18:
    if driv_lic == True:
        print("person can drive")
    else:
        print("driv_lic==false")
else:
    print("person connot drive")


# 5 Write a program to check ATM withdrawal.If the account balance is greater than or equal to the withdrawal amount, check whether the withdrawal amount is within the daily limit.
bal_amt=30000
dly_limt=15000
withdrawl_amt=10000
if bal_amt>=withdrawl_amt:
    if withdrawl_amt<dly_limt:
        print("transcation successfull")
    else:
        print("limit exceeded")
else:
    print("insufficient balance")


# Medium Level 

# 6  Write a program to determine an employee's bonus. If the employee has worked for at least 5 years, check if the performance rating is "Excellent".Give a higher bonus for excellent performance; otherwise, give a standard bonus.
years=6
rating="good"
if years>=5:
    if rating == "excellent":
        print("higher bonus")
    else:
        print("standard bonus")
else:
    print("not eligible for bonus")


# 7 Write a program to determine whether a student is eligible for a scholarship. If the student's attendance is at least 75%, check whether the marks are 90 or above.
attnd=74
marks=92
if attnd >= 75:
    if marks >= 90:
        print("eligible for scholarship")
    else:
        print("not eligible becoz marks are below 90")
else:
    print("not eligible becoz attnd is below 75")


# 8 Write a program to check admission eligibility. If the candidate has passed the entrance exam, check whether their age is between 17 and 25.
exam="pass"
age=21
if exam == "pass":
    if age >= 17 and age <= 25:
        print("eligible")
    else:
        print("age is not valid")
else:
    print("not eligible bcoz exam is fail")


# 9  Write a program to determine whether an online order qualifies for free delivery.If the purchase amount is at least ₹1000, check whether the customer is a premium member.
purs_amt=1500
cust="premium"
if purs_amt>=1000:
    if cust == "premium":
        print("free delivery")
    else:
        print("not deliver bcoz cust is not premium")
else:
    print("not deliver becoz purs_amt is not>=1000")

# 10 Write a program to check if a bank loan can be approved. If the applicant's salary is at least ₹30,000, check whether their credit score is 750 or above.
sal=35000
crd_scr=800
if sal>=30000:
    if crd_scr == 750:
        print("loan approved")
    else:
        print("crd_scr is not > 750")
else:
    print("sal is below 30000")


# 11  Write a program to determine a movie ticket price.If the person is a student, check whether they are under 18 to provide an additional discount.
per="student"
age=21
if per=="student":
    if age>=18:
        print("discount")
    else:
        print("no discount becoz age <18")
else:
    print("no discount per is not student")


# 12 Write a program to determine hostel eligibility.If the student belongs to another city, check whether hostel rooms are available.
std= input("do you belongs to another city (yes/no):")
rooms=input("available(yes/no)")
if std == 'yes':
    if rooms == 'yes':
        print("eligible")
    else:
        print("not eligible becoz rooms are not available")
else:
    print("not eligible becoz std belongs to same city")


# 13  Write a program to determine promotion eligibility.If an employee has completed at least 3 years of service, check whether the performance rating is at least 4.
years=int(input("enter years of experience:"))
rating=int(input("enter performance rating:"))
if years >= 3:
    if rating >= 4:
        print("eligible")
    else:
        print("not eligible becoz rating <4")
else:
    print("not eligible becoz years<3")

# 14 Write a program to check exam eligibility.If attendance is at least 75, check whether the assignment marks are at least 40.
attnd=int(input("enter your attnd:"))
marks=int(input("enter your marks:"))
if attnd >=75:
    if marks >=40:
        print("eligible")
    else:
        print("not eligible becoz marks < 40")
else:
    print("not eligible becoz attnd <75")