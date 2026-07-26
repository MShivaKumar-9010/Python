#1. Check whether a number is positive, negative, or zero 
number=int (input("enter the num:"))
if number>0:
    print("number is positive")
elif number<0:
    print("number is negative")
else:
    print("number is zero")


# 2. Check whether a number is even or odd  
number=int(input("enter the number:"))
if number%2==0:
    print("even")
else:
    print("odd")


#3. Find the largest of two numbers  
value1=int(input("enter the number1:"))
value2=int(input("enter the number2:"))
if value1>value2:
    print("value1 is largest")
else:
    print("value2 is largest")


#4. Find the largest of three numbers  
val1=int(input("enter the number1:"))
val2=int(input("enter the number2:"))
val3=int(input("enter the number3:"))
if val1>val2 and val1>val3:
    print("val1 is largest")
elif val2>val1 and val2>val3:
    print("val2 is largest")
else:
    print("val3 is largest")


#5. Check whether a person is eligible to vote (age ≥ 18)
age=int(input("enter your age:"))
if age>=18:
    print("eligible")
else:
    print("not eligible")


#6. Assign grades based on marks (A, B, C, Fail) 
marks=int(input("enter your marks:"))
if marks>=95:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=60:
    print("grade C")
else:
    print("fail")


#7. Check whether a character is vowel or consonant  
name="b"
if name=="a" or name=="e" or name=="i" or name=="o" or name=="u":
    print("vowels")
else:
    print("consants")


#8. Check whether a number is divisible by both 3 and 5  
num=12
if num%3==0 and num%5==0:
    print("num is divisibly by 3 and 5")
else:
    print("num is not divisibly by 3 and 5")


#9. Check whether a character is uppercase, lowercase, digit, or special symbol  
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special symbol")


#10. Check whether a number is divisible by 7 
val=int(input("enter the number:"))
if val%7==0:
    print("divisible by 7")
else:
    print("not divisible by 7")


#11. Check whether a person is a senior citizen (age ≥ 60)  
age=int(input("enter your age:"))
if age>=60:
    print("senior citzen")
else:
    print("not senior citzen")


 #12. Check whether a year is a leap year  
year=int(input("enter the year:"))
if year%4==0:
    print("leaf year")
else:
    print("not a leaf year")


#13. Build a *simple calculator (+, -, , /)  
a=int(input("enter the value:"))
b=int(input("enter the value:"))
operator=input("enter opertor:")
if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '/':
    print(a / b)
else:
    print("entered invalid ")


#14. Check whether a number is in range (1 to 100)  
val=int(input("enter the number:"))
if val>=1 and val<=100:
    print("number is in range 1 to 100")
else:
    print("not in range 1 to 100")


#15. Input marks of 3 subjects and check pass/fail (≥35 each)  
maths=36
python=45
sql=34
if maths>=35 and python>=35 and sql>=35:
    print("pass")
else:
    print("fail")    


# 16. Check whether a number is a multiple of 3 and 5 (separately)  
num=3
if num%3==0 and num%5==0:
    print("num is multi of 3 and 5")
else:
    print("num is not multi of 3 and 5")


#17. Simulate ATM withdrawal (check sufficient balance)  
withdrawl_amount=int(input("enter the amount:"))
balance=30000
if withdrawl_amount<=balance:
    print("transaction successful")
else:
    print("transaction failed insufficient funds")


#18. Calculate tax based on salary slabs  
sal=float(input("enter the salary:"))
if sal<=100000 :
    print("no tax")
elif sal>200000:
    print("tax=",sal*5/100)
elif sal>300000:
    print("tax=",sal*10/100)
else:
    print("tax=",sal*20/100)


#19. Check whether a number is a 3-digit number  
num = int(input("enter the number:"))
if num in range(100,1000):
    print(num,"is a 3digit number")
else:
    print(num,"is not a 3digit number")
        

#20. Check whether a character is an alphabet (without built-in functions)  
ch = input("Enter a character: ")

if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print("an alphabet")
else:
    print("not an alphabet")


#21. Find the largest of three numbers using nested if  
a = 25
b = 35
c = 20
if a > b:
    if a > c:
        print("a is largest")
    else:
        print("c is largest")
else:
    if b > c:
        print("b is largest")
    else:
        print("c is largest")
    

# 22. Create a login system (username & password check)  
ch=input("enter username:")
ch2=input("enter password:")
if ch=="10k" and ch2=="coders10":
    print("login system ")
else:
    print("invalid username or password")


#23. Check whether a number is positive → then check even/odd  
num=int(input("enter the number:"))
if num>0:
    if num%2==0:
     print("positive even")
    else:
        print("positive odd")
else:
    print("negative")
    
    
#24. ATM system with conditions (balance + withdrawal limit)  
balance=30000
withdrawl_limit=15000
withdrawl_amount=int(input("enter the amount:"))
if balance>=withdrawl_amount and withdrawl_limit>=withdrawl_amount:
    print("transaction successful")
else:
    print("transaction exceeded")


#25. Student result system:  • Pass (≥35)  • Distinction (≥75)  • First Class (≥60)
marks=int(input("enter your marks:"))
if marks>=75:
    print("distinction")
elif marks>=60:
    print("first class")
elif marks>=35:
    print("pass")
else:
    print("fail")