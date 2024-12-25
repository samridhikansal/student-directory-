from master import student



def update(id):
   
    
    for s in student:
       
        if s["id"]==id:
            
            print ("The student with the id ", {id}, "found.")

            print("The id of the student can't be changed or updated. You can only update the name of the student.")
            name = str(input ("Enter the name now:")) 
            s["name"]= name
            print("\nThe name of the student has been updated successfully. Here is the updated list of the students in the system")
            for s in student:
                print (s["id"], s["name"])
    return student




