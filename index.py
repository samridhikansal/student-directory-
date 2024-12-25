
from master import student
from add_student import add_student
#from sub_student import sub_student
from view_student import view_student
from update import update

print("Welcome to the student managemnet system. \n Here are the list of the students in the system")
for s in student:
    print(s["id"], s["name"])
print("Press 1 for adding a student \n Press 2 for deleting a student \n Press 3 for updating the student \n Press4 for viewing the deatils of the student")
choice = int(input("\nEnter your Choice Now:"))
if choice == 1:
    print("You have selected to add the student. Please enter the id and the name of the student")
    id = int(input("Enter the id of the student:"))
    name = str(input ("Enter th name of the student"))
    add_student(id,name)
#elif choice ==2:
    #print("You have selected to delete the student. \nPlease enter the id  and the name of the student you want to delete")
   # id = int(input("Enter the id of the student:"))
    #sub_student(id)
    
elif choice ==3:
    print("You have selected to update the student")
    id = int(input("\n Enter the id of the student you want to update:"))
    update(id)
elif choice ==4 :
    print ("You have selected to view the student details")
    id = int(input("\nEnter the id of the student you want the details about:"))
    view_student(id)
else:
    print("You have selected the wrong choice. Try again")

#this file has all the logic. This is main file. 
#This file is importing all the modules and executing the code as per the user input 

