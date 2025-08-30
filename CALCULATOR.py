print("1 = Addition")
print("2 = Substraction")
print("3 = Multiplication")
print("4 = Division")

option = int(input("Choose An operation : "))
result = 0

if (option in [1,2,3,4]):
    num1 = float(input("Enter 1st Number : "))
    num2 = float(input("Enter 2nd Number : "))

    if(option==1):
        result = num1 + num2
    elif(option==2):
        result = num1 - num2
    elif(option==3):
        result = num1 * num2    
    elif(option==4):
        result = num1 / num2


else:
    print("Invalid Operation Entered")

print("The Result Of The Operation Is {} ", result)    