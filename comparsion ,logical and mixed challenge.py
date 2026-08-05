
# Comparison Operators

# Q1: Rahul scored 78 marks. The passing mark is 35. Write a Python expression to check whether Rahul passed.
rahul_marks = 78
pass_marks = 35
passed = rahul_marks >= pass_marks
print(passed)
# OUTPUT: True (Rahul passed)


# Q2: A movie ticket is allowed only for people aged 18 or above. A person's age is 16. Check eligibility.
age = 16
age_eligible = age >= 18
print(age_eligible)
# OUTPUT: False (Not eligible)


# Q3: A laptop costs ₹55,000. Your budget is ₹60,000. Check whether the laptop is within your budget.
laptop_cost = 55000
budget = 60000
within_budget = laptop_cost <= budget
print(within_budget)
# OUTPUT: True (Yes, he can buy the laptop)


# Q4: There are 25 students in Class A and 25 students in Class B. Check whether both classes have the same number of students.
class_A = 25
class_B = 25
students = class_A == class_B
print(students)
# OUTPUT: True


# Q5: The temperature today is 42°C. Check whether the temperature is greater than 40°C.
today_temp = 42
given_temp = 40
whether = today_temp > given_temp
print(whether)
# OUTPUT: True


# Q6: A customer entered the correct OTP 5678. The entered OTP is 6789. Check whether the OTP is incorrect.
correct_otp = 5678
entered_otp = 6789
customer_otp = correct_otp != entered_otp
print(customer_otp)
# OUTPUT: True (Incorrect OTP)


# Q7: The speed limit is 80 km/h. A car is moving at 80 km/h. Check whether the car is following the speed limit.
speed_limit = 80
car_speed = 80
following_limit = car_speed <= speed_limit
print(following_limit)
# OUTPUT: True


# Q8: A train has 150 seats. Currently, 145 seats are booked. Check whether all seats are filled.
train_seats = 150
booked_seats = 145
all_seats = train_seats == booked_seats
print(all_seats)
# OUTPUT: False


# Q9: The minimum balance required is ₹1000. Current balance is ₹850. Check whether balance is less than the required amount.
min_balance = 1000
current_balance = 850
required_amount = current_balance < min_balance
print(required_amount)
# OUTPUT: True


# Q10: A student needs at least 75% attendance. Current attendance is 75%. Check eligibility.
min_attendance = 75
current_attendance = 75
student_attend = current_attendance >= min_attendance
print(student_attend)
# OUTPUT: True (Eligible)



# Logical Operators


# Q11: A student can attend the placement drive only if CGPA >= 7.5 and Attendance >= 75%.
cgpa = 8.1
attendance = 82
eligible = cgpa >= 7.5 and attendance >= 75
print(eligible)
# OUTPUT: True


# Q12: Free delivery if Purchase > ₹500 and Prime Member.
purchase = 650
prime_member = True
free_delivery = purchase > 500 and prime_member
print(free_delivery)
# OUTPUT: True


# Q13: Login allowed if Username is correct OR Email is correct.
username_correct = False
email_correct = True
login_allowed = username_correct or email_correct
print(login_allowed)
# OUTPUT: True


# Q14: Cricket player selected if Runs > 500 and Wickets > 20.
runs = 620
wickets = 18
selected = runs > 500 and wickets > 20
print(selected)
# OUTPUT: False (Player not selected)


# Q15: Student passes only if Theory >= 35 and Practical >= 35.
theory = 40
practical = 30
student_pass = theory >= 35 and practical >= 35
print(student_pass)
# OUTPUT: False (Student fails)


# Q16: Discount if Member OR Purchase > ₹2000.
member = False
purchase = 2500
discount = member or purchase > 2000
print(discount)
# OUTPUT: True


# Q17: A person can vote if Age >= 18 and Citizen.
age = 20
citizen = True
can_vote = age >= 18 and citizen
print(can_vote)
# OUTPUT: True


# Q18: Student is not absent.
absent = False
present = not absent
print(present)
# OUTPUT: True


# Q19: Admin access if Username is "admin" and Password is correct.
username = "admin"
password_correct = True
admin_access = username == "admin" and password_correct
print(admin_access)
# OUTPUT: True


# Q20: Swimming pool entry if Membership OR Paid Fee.
membership = False
paid_fee = False
can_enter = membership or paid_fee
print(can_enter)
# OUTPUT: False


# ==========================
# Mixed Comparison + Logical Operators
# ==========================

# Q21: Grade A if Marks are between 90 and 100 (inclusive).
marks = 95
grade_A = marks >= 90 and marks <= 100
print(grade_A)
# OUTPUT: True


# Q22: Cashback if Purchase >= ₹1000 and Purchase <= ₹5000.
purchase = 3200
cashback = purchase >= 1000 and purchase <= 5000
print(cashback)
# OUTPUT: True


# Q23: Password reset if OTP is correct and Account is active.
otp_correct = True
account_active = True
reset_password = otp_correct and account_active
print(reset_password)
# OUTPUT: True


# Q24: Player qualifies if Age is between 18 and 25 (inclusive).
age = 23
player_qualifies = age >= 18 and age <= 25
print(player_qualifies)
# OUTPUT: True


# Q25: Vehicle fined if Speed > 80 OR Signal Broken.
speed = 75
signal_broken = True
fine = speed > 80 or signal_broken
print(fine)
# OUTPUT: True


# ==========================
# Challenge Questions
# ==========================

# Q26: Check whether a number is between 10 and 50 (inclusive).
num = 35
condition = num >= 10 and num <= 50
print(condition)
# OUTPUT: True


# Q27: Check whether a person is either a student or a teacher.
is_student = True
is_teacher = False
person = is_student or is_teacher
print(person)
# OUTPUT: True


# Q28: Check whether a password length is at least 8 characters and contains at least one digit.
password = "Python123"
condition = len(password) >= 8 and any(char.isdigit() for char in password)
print(condition)
# OUTPUT: True


# Q29: Check whether a person's age is not less than 18.
age = 18
condition = age >= 18
print(condition)
# OUTPUT: True


# Q30: Customer gets a gift if Purchase > ₹5000 AND Premium Member AND Birthday.
purchase = 6000
premium_member = True
birthday = True
gift = purchase > 5000 and premium_member and birthday
print(gift)
# OUTPUT: True