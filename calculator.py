print("WELCOME TO YOUR CALCULATOR")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calc():
    first_num = float(input("Input a number: \n"))
    still_calculating = True

    while still_calculating:
        operation = input("Choose an operation using (+ * - /): \n")
        num = float(input("Input another number: \n"))
        # a new variable that selects the users operation and assign it to the key on the operations dictionary
        operation_func = operations[operation]
        answer = operation_func(first_num, num)
        print(answer)
        user_question = input(f"Type 'Yes' to keep calculating with {answer} or 'No' to start a new calculator : \n")
        # assigns the answer to the first num so that the calculation continues but with first_num been the answer
        if user_question == 'Yes'.lower():
            first_num = answer
        # starts a new calculator
        elif user_question == 'No'.lower():
            calc()
        else:
            # breaks out of the loop. And exits the calculator
            print("Wrong input")
            still_calculating = False

calc()
























































