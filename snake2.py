from colorama import Fore,init
n=int(input("n="))
flag=0
for i in range(n):
    if(flag==0):
       print(Fore.GREEN,"*",end=" ")
       flag=1
    elif(i in range(1,n,2)):
        print(Fore.YELLOW,"*",end=" ")
        flag=0
