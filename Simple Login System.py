credential={
    "admin":"admin123",
    "sara": "imsara44",
    "ali": "1234",
}
username=input("Enter username: ")
if username in credential:
    attempt=0
    while attempt < 3:
        password=input("Enter password: ")
        if credential[username]== password :
           print("login successfull")
           break
        elif credential[username]!= password:
            print("incorrect password, try again!")
            attempt=attempt+1
    if attempt >=3:
        print("Account locked !")        
        
else:  
    print("user not found")  

