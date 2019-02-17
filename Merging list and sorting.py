#Merging two List and sorting it 

list1=[]
x=int(input("How many elements you want in list 1:"))
for i in range(x):
    a=int(input("Enter the Element:"))
    list1.append(a)
    
list2=[]
y=int(input("How many elements you want in list 2:"))
for j in range(y):
    b=int(input("Enter the Element:"))
    list2.append(b)
    
list3=list1+list2

list3.sort()

print("The Merged and Sorted List is:",list3)
