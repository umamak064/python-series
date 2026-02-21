record=[]
while True:
    user_option=input("1. Add Student \n 2. Search Student \n 3. Update Student\n 4. Delete Student \n 5. Exit \n Enter your choice: " )

    if user_option=="1":

        while True:
            #sub list ko loop k andr rakhein ge otherwise sub students k record ik hi sub list me add hotay raheinge like this [['sara', 22, 'a', 'ali', 33, 'a'], ['sara', 22, 'a', 'ali', 33, 'a']]
            student=[]
        #Create
            name=input("Enter name: ")
            student.append(name)
            age=int(input("Enter age: "))
            student.append(age)
            Grade=input("Enter Grade: ")
            student.append(Grade)
            option=input("Enter add to add more student otherwise enter stop: ")
            record.append(student)
        
            if option=="stop":  
                #READ
                print(record)
                break
    elif user_option=="2":        
        #Search
        key =input("Enter name to search: ")
        found=False
        for st in  record:
            if (key==st[0]):
                #student[0]=name, student[1]=age, student[2]=grade
                print(st[0],st[1],st[2])
                found=True
                break
        if not found:    
            print("This name student not exist!")
    
    elif user_option=="3":    
        #update
        nameToUpdate=input("Enter name you want to update: ")    
        found=False
        for i in record:
            if nameToUpdate==i[0]:
                
                newName=input("Enter new name: ")
                i[0]=newName
                print(record)
                found=True
        if not found:
            print("Student not found")      
    elif user_option=="4":    
        #delete
        
        del_name=input("enter name you want to delete: ")
        
        found=False
        for i in record:
            if del_name==i[0]:
                record.remove(i)
                print(record)
                found=True
                break
        if not found:
            print("Student not found")  
    elif user_option=="5":       
        break   
        
    
    
    
    
    
    
    