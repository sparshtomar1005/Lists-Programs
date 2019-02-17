#seperate Even and Odd Elements in lists
Elements=[]
x=int(input("How many elements you want in List:"))
for i in range(x):
    a=int(input("Enter the Element:"))
    Elements.append(a)

Even=[]
Odd=[]

for j in Elements: 
    if(j%2==0):
        Even.append(j)
    else:
        Odd.append(j)

print("Even List:",Even)
print("Odd List:",Odd)
        
