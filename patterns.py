#pattern 1: Right Triangle
n=6
for i in range(n):
    for j in range(i):
        print("*",end="")
    print()

#Pattern 2: Inverted Right Triangle
n=6 
for i in range(n): 
    for j in range(i,n-1): 
        print("*",end='') 
    print()     

#Pattern 3: Right Aligned Triangle
n=6 
for i in range(n): 
    for j in range(i,n-1): 
        print(" ",end='') 
    for k in range (i):
        print("*",end="")
    print()     
#Pattern 4: Inverted Right Aligned Triangle
n=6 
for i in range(n): 
    for j in range(i): 
        print(" ",end='') 
    for k in range (i,n-1):
        print("*",end="")
    print()     
#Pattern 5: Pyramid 

n=6 
for i in range(n): 
    for j in range(i,n-1): 
        print(" ",end='') 
    for k in range (2*i+1):
        print("*",end="")
    print()     

#Pattern 5: Inverted Pyramid

n=6 
for i in range(n): 
    for j in range(i): 
        print(" ",end='') 
    for k in range (2*(n-i)-1):
        print("*",end="")
    print()    

#Pattern 7: Number Pattern 
n=6 
for i in range(n): 
    for k in range (i):
        print(k+1,end="")
    print()     

#Pattern 8: Repeated Numbers
n=6 
for i in range(n): 
    for k in range (i):
        print(i,end="")
    print()  

#Pattern 9: Floyd’s Triangle    
n=5 
count=1
for i in range(n): 
    for k in range (i):
        print(count,end=" ")
        count=count+1
    print()     