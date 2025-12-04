n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
op = input("Choose the operator (+, -, *, /): ")
match op :
    case "+" :
        print(f"the result is {n1 + n2}")
    case "-" :
        print(f"the result is {n1 - n2}")
    case "*" :
        print(f"the result is {n1 * n2}")
    case "/" :
        if n2 != 0:
            print(f"the result is {n1 / n2}")
        else: 
            print("Cannot divide by zero.")
    case _ :
        print("unknown operator")
      
