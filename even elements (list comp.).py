#Taking only even elements from a list and putting it in different list using list comprehensions

list=[]
x=int(input("How many Elements you want in List:"))
for i in range(x):
    a=int(input("Enter the Element:"))
    list.append(a)

even=[a for a in list if a%2==0]
even.sort()    
print("Even List:",even)    