#taking input from user
while True:
    print("Enter two nubers:")
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("Coose an option from below:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    operation=int(input("Enter your choice:"))
    if(operation in [1,2,3,4,5]):
#performing action based on user input
        if operation==1:
            result=num1+num2
            print("Sum:",result)
        elif operation==2:
            result=num1-num2
            print("Difference:",result)
        elif operation==3:
            result=num1*num2
            print("Product:",result)
        elif operation==4:
            if num2!=0:
                result=num1/num2
                print("Quotient:",result)
            else:
                print("Cannot divide by zero")
        elif operation==5:
             print("Exiting")
             break
#exiting is entered an invalid choice
else:
    print("Invalid choice")

        

        
