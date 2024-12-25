from master import student

id = int(input("Enter id")) 

def sub_student(id):
   
    print("Hello")
    for s in student:
        print("I am in for loop")
        if s["id"]==id:
            print("I am in if loop")
            print ("The student with the id ", {id}, "found.")
            s.remove(s["id"])
            print("The student has been removed from the system")
            print("Here is the updated list of the students in the system")
            for s in student:
                print(s["id"], s["name"])
    return student
sub_student(id)



