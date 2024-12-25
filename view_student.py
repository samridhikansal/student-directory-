from master import student



def view_student(id):
   for s in student:
         if s["id"]==id:
            print ("The student with the id ", {id}, "found.")
        
            print("The id of the student is ", s["id"])
            print("The name of the student is ", s["name"])
            break
   for s in student:
         if s["id"]!=id:
          print("The student with the id",{id}, "not found. Please check your id and try again")
   return()




