num=int(input("Enter number here: "))
if 0 <=num<=100:
    if  num >= 90: 
        print("Grade A+")
    elif num >= 80: 
        print("Grade A")   
    elif num >= 70: 
        print("Grade B") 
    elif num >= 60: 
        print("Grade C") 
    elif num >= 40: 
        print("Grade D")      
    else:
        print("fail")          
else:
    print("invalid number")


