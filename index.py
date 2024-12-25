
from master import student
from add_student import add_student
from sub_student import sub_student
from view_student import view_student
from update import update

print("\nWelcome to the student managemnet system. \n Here are the list of the students in the system\n. Here is the list of some of the functions that you can perform on the students database")
# the system prints the list of all the students to begin with 
for s in student:
    print(s["id"], s["name"])

# the system prints the list of all the oprrations along with the instructions 
print("\nPress 1 for adding a student \n Press 2 for deleting a student \n Press 3 for updating the student \n Press4 for viewing the deatils of the student")
choice = int(input("\nEnter your Choice Now:"))

# the system takes the input from the user and perform the appropriate operation
if choice == 1:
    print("You have selected to add the student. Please provide the details of the student")
    id = int(input("Enter the id of the student:"))
    name = str(input ("Enter th name of the student"))
    add_student(id,name)
elif choice ==2:
    print("You have selected to delete the student\n")
    id = int(input("Enter the id of the student you want to remove:"))
    sub_student(id)
    
elif choice ==3:
    print("You have selected to update the student")
    id = int(input("\n Enter the id of the student you want to update:"))
    update(id)
elif choice ==4 :
    print ("You have selected to view the student details")
    id = int(input("\nEnter the id of the student you want the details about:"))
    view_student(id)
else:
    print("You have selected the wrong choice. So, we are unable to perform any operation. Try again")

#this file has all the logic. This is main file. 
#This file is importing all the modules and executing the code as per the user input 

