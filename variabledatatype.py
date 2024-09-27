#we use multiple datatypes to store the info with variable

#name variable should be stored in string datatype
name = "Raj"

#email address are stored in the form of string
email = "raj@gmail.com"

#age variable is stored in int datatype
age = 21

#phone number is stored in int datatype
phone_number = 9888778888

#height is stored in float datatype
height = 6.1

#is_student is stored as boolean datatype
is_student = True

# skills are stored in list
skills = ["Java","python","cpp","html","css","javascript"]

#the display method is used to display every detail
def display():
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"Phone Number: {phone_number}")
    print(f"Height: {height}")
    print(f"Is he a Student: {is_student}")
    print("Skills: ",skills)

#display method is called
display()