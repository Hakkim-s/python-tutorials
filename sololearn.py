while True :

    print("Add")
    print('sub')
    print('mul')
    print('div')
    print("quit \n " )
    user_input = input("Enter the option from above : \n" )

    if user_input == "quit":
     break
    elif user_input == "add":
        num1 = int(input("Enter the number:"))
        num2 = int(input("Enter the number2:"))
        results =str(num1 + num2)
        print("Answer = " + results)
        break
    elif user_input == "sub":
        num1 = int(input("Enter the number:"))
        num2 = int(input("Enter the number2:"))
        results =str(num1 - num2)
        print("Answer = " + results)
        break
    elif user_input == "mul":
        num1 = int(input("Enter the number:"))
        num2 = int(input("Enter the number2:"))
        results =str(num1 * num2)
        print("Answer =" + results)
        break
    elif user_input == "div":
        num1 = int(input("Enter the number:"))
        num2 = int(input("Enter the number2:"))
        results = str(num1 / num2)
        print("Answer = " + results)
        break
    else :
        print("Choose only from 5 above options")
        break