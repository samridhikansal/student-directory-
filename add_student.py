from master import student 
def add_student(id,name):
    student.append({"id":id,"name":name})
    print("student added successfully \n Here is the update list of the students in the system")
    for s in student:
        print(s["id"], s["name"])
    return student
