a=float(input("Enter 1st Number"))
b=float(input("Enter 2nd Number"))

print("1. adddition ")
print("2. subtarction ")
print("3. multipilication ")
print("4. division ")
print("5. modulo ")

c=int(input("Select Operation to perform"))

if c==1:
    print(a,"+",b," = ",a+b)
elif c==2:
    print(a,"-",b," = ",a-b)   
elif c==3:
    print(a,"x",b," = ",a*b)  
elif c==4:
    print(a,"/",b," = ",a//b)  
elif c==5:
    print(a,"%",b," = ",a%b)  
else:
    print("Wrong Selection ")