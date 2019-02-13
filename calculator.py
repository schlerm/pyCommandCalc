def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def times(x, y):
    return x*y

def divide(x, y):
    return x/y

def calc():
    operator = str(input("Select an operation (+,-,*, or /)"))
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    if operator == "+" :
        print(num1,"+",num2,"=",plus(num1, num2))
    elif operator == "-" :
        print(num1,"-",num2,"=",minus(num1, num2))
    elif operator == "*" :
        print(num1,"*",num2,"=",times(num1, num2))
    elif operator == "/" :
        print(num1,"/",num2,"=",divide(num1, num2))
    else:
        return("This ain't it chief.")
    cont = input("Continue? y or n")
    if cont == "y":
        calc()
    else:
        return("Bye")

calc()