#Create a Python function named calculate_area that takes the radius of a circle as an argument and returns the area of the circle.
#Implement another function named calculate_circumference that takes the radius of a circle as an argument and returns the circumference of the circle.
#Write a main function named main where you call calculate_area and calculate_circumference with a radius of your choice and print the results.
#Ensure your code is well-structured, readable, and includes comments to explain what each function does.
#Submit your Python script as a .py file.

def calculated_area(radius):
    x=3.14*radius**2 #pi value is 3.14
    print("area of circle:",x)
# calculated_area(5)

def circumference(radius):
    y=2*3.14*radius  # pi value is 3.14
    print("circumference of circle:",y)
# circumference(15)

def main():
    calculated_area(5)
    circumference(15)
main()