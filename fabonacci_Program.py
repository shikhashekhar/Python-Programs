def fabonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)

number = int(input("Enter a number for fabonacci series:- "))
print(fabonacci(number)) # this will give fabonnaci series sum value
for i in range (number):
    print(fabonacci(i),end=", ") # This will give fabonacci sequence
