#Generate a formatted full name
def formatted_name(first_name, last_name):
   full_name = first_name + ' ' + last_name
   return full_name.title()

from name_function import formatted_name

print ("Please enter the first and last names or enter x to E[x]it.")

while True:
    first_name = input("Please enter the first name: ")
    if first_name == "x":
        print("Good bye.")
        break

        last_name = input ("Please enter the last name: ")
        if last_name == "x":
            print("Good bye.")
            break
            
        result = formatted_name(first_name, last_name)
        print ("Formatted name ist: " + result + ".")

        