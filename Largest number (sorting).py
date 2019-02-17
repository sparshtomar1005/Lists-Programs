#Find the Largest number
Numbers=[]
x=int(input("Enter the no of elements in List:"))
for i in range(x):
    a=int(input("Enter the Element:"))
    Numbers.append(a)
Numbers.sort()
Numbers.reverse()
print("The Largest number is :",Numbers[0])
    

