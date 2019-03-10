#Generate a dictionary from two list
list1=[]
a=int(input("Enter the no of elements you want to put in list 1:"))
for i in range(a):
    x=input("Enter the Element:")
    list1.append(x)    
    
    
list2=[]
b=int(input("Enter the no of elements you want to put in list 2:"))
for j in range(b):
    y=input("Enter the Element:")
    list2.append(y)
    
print("List 1 is:",list1)
print("List 2 is:",list2)

dict=dict(zip(list1,list2))

print("The Dictionary is:",dict)