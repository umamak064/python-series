balance=int(input("Enter balance: "))
amount=int(input("Enter amount here: "))
if amount> balance:
    print("Insufficient balance")
elif amount<=0 :
    print("Invalid amount")
else:
    remains=balance - amount
    print("Trasaction successfully!", amount ,"is debited")
    print("remaining balance is ", remains)



