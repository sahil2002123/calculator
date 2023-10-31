n1= int(input ("Enter 1st number:  "))
operator = input ("Enter your operator:   ")
n2 = int(input("Enter your second number:  "))

match operator:
    case "+" : print("The sum of two numbers is :  ", n1+n2)
    case "-" : print("The subtraction of two numbers is  ", n1-n2)
    case "*" : print("The multiplication of two numbers is  ", n1*n2)
    case "/" : print("The divison of  two numbers is  ", n1/n2)
    case _ : print("Enter a valid operator ")