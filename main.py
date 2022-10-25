def cali(operation_value, numb1, numb2):
    result = 0.0
    if operation_value == "+":
        result = numb1 + numb2

    elif operation_value == "-":
        result = numb1 - numb2

    elif operation_value == "*":
        result = numb1 * numb2

    elif operation_value == "/":
        result = numb1 / numb2

    return result


while True:

    try:
        num1 = float(input("Enter Your input one: "))
    except ValueError:
        print("Sorry, I didn't understand that!!")
        break

    # -------------------------

    operation = input("Enter operation: ")
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":

        try:
            num2 = float(input("Enter Your input two: "))
        except ValueError:
            print("Sorry, I didn't understand that!!")
            break

    else:
        print("I don't understand what operation it this!? ")
        break

    # -------------------------

    c = cali(operation, num1, num2)
    print(f"Result is {c}")
    print("-------------------------------------")
