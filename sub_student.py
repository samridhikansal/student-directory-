from master import student


def sub_student(id):
   
    for s in student:
        
        if s["id"]==id:
            student.remove(s)
            print ("The student record with the id", {id}, "found and deleted")
            print("\nHere is the update list of the students in the system")
            for s in student:
                print(s["id"], s["name"])
    return




