#Taking only even elements from a list and putting it in different list 

list=[]
x=int(input("How many Elements you want in List:"))
for i in range(x):
    a=int(input("Enter the Element:"))
    list.append(a)

even=[]
for a in list:
    if(a%2==0):
        even.append(a)
    else:
        continue
    
even.sort()    
print("Even List:",even)    