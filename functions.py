# Create a function that prints "Hello, World!".
def google():
    print("Hello,World")
google()


# Create a function that prints your name.
def person(name):
    print(name)
person("M Shiva Kumar")


# Create a function that prints today's date.
def calender(todays_date):
    print(todays_date)
calender("05/08/2026")
             
   
# Create a function that prints numbers from 1 to 10.
def number(n):
    for i in range (1,n+1):
        print(i)
number(10)        


# Create a function that prints the multiplication table of 5.
def multiply():
    for i in range(1,11):
        print(f"{5}x {i} ={5*i}")
multiply()      

def multi_5(n):
    for i in range(n,n+1):
        for j in range(1,11):
            print(i,"x",j,"=",i*j)
multi_5(5)

def table_5():
    for i in range(1,11):
        print(5,"*",i,"=",5*i)
table_5()    

   
# Create a function that prints all even numbers from 1 to 20.
def num(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)
num(20)


# Create a function that prints all odd numbers from 1 to 20.
def num(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i)
num(20)


# Create a function that prints a square pattern of stars (4 × 4).
def pattern(n):
    for i in range(1,n+1):
        stars=''
        for j in range (1,n+1):
            stars+="* "
        print(stars)
pattern(4)


# Create a function that prints a right-angled triangle of stars.
def pattern(n):
    for i in range(1,n+1):
        stars=''
        for j in range(1,i+1):
            stars+="* "
        print(stars)
pattern(4)


# Create a function that prints the message "Welcome to Python Programming".
def greet(name):
    print(name,)
greet("Welcome to Python Programming")


# Create a function that takes a name and prints a welcome message.
def wish(name):
    print("Welcome",name)
wish("shiva")


# Create a function that takes two numbers and prints their sum.

def add(a,b):
    print(a+b)
add(2,3)


# Create a function that takes two numbers and prints their difference.
def sub(x,y):
    print(x-y)
sub(17,13)


# Create a function that takes two numbers and prints their product.
def mul(p,q):
    print(p*q)
mul(3,7)


# Create a function that takes two numbers and prints their division.
def div(a,b):
    print(a/b)
div(10,5)


# Create a function that takes a number and prints its square.
def square(i):
    print(i**2)
square(9)


# Create a function that takes a number and prints its cube.
def cube(i):
    print(i**3)
cube(3)


# Create a function that takes a number and checks whether it is even or odd.
def num(i):
        if i%2==0:
            print('even')
        else:
            print('odd')
i=int(input("enter the num:"))
num(i)


# Create a function that takes a number and checks whether it is positive or negative.
def num(i):
    if i > 0:
        print('positive')
    elif i < 0:
        print('negative')
    else:
        print('Zero')
i=int(input("enter the num:"))   
num(i)


# Create a function that takes a string and prints its length.
def length(name):
    print(len(name))
length("shiva")
    