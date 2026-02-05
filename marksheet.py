#Marksheet
Sub1=float(input("Enter subject 1 marks: "))
Sub2=float(input("Enter subject 2 marks: "))
Sub3=float(input("Enter subject 3 marks: "))
Sub4=float(input("Enter subject 4 marks: "))
Sub5=float(input("Enter subject 5 marks: "))

Marks= Sub1+Sub2+Sub3+Sub4+Sub5
print("Your marks is", Marks)
percentage= (Marks/500) * 100
print("Your perentage is", percentage)

if  percentage >=80:
    print ("Grade is A")
elif percentage >= 60:
    print ("Grade is B")
elif percentage >= 40:
    print ("Grade is C")   
else:
    print("You are fail")