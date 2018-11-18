'''try:
    num1 = 5
    num2 = 0
    print(num1/num2)
except ZeroDivisionError:
    print("zero division error")
finally:
    print("this code will excecute whatever happens")
'''
    try:
        print("Hello")
        print(1 / 0)
    except ZeroDivisionError:
        print("Divided by zero")
    finally:
        print("This code will run no matter what")
try:
    x = int(input("enter integer : "))
    #this line says if x is string type
    if isinstance(x, str):
        raise ValueError

    print("x * 5 = ",x * 5)
except ValueError:
    print("The hell did you entered")
