a=[]
b=[]
for i in range(5):
    n=int(input("Enter number:"))
    a.append(n)
    b.append(n)
b.sort()
if(a==b):
    print("This is a sorted array")
else:
    print("This is not a sorted array")
    


