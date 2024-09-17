age=int(input("Enter a age: "))
if(age==0):
    print("Its a new born baby")
elif(age>0):
    if(age>0 and age<15):
        print("Person cannot drive")
    elif(age==15):
        print("Person can learn driving but not drive anywhere on road")
    elif(age>15 and age<=18):
        print("Person is eligible for G2 license but with limited driving options")
    else:
        print("The person can drive with valid driving license")
else:
    print("This is unknown Condition")