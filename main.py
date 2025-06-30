history_file = "history.txt"

def show_history():
    file = open(history_file, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("Your history is empty! Perform calculations to see history.")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(history_file, 'w')
    file.close()
    print("History Cleared !")

def save_history(expression, result):
    file = open(history_file, 'a')
    file.write(expression + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input.")
        return
    
    num1 = float(parts[0])
    num2 = float(parts[2])
    op = parts[1]
    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '/':
        if num2 == 0:
            print("Cannot divide zero.")
            return
        res = num1 / num2
    elif op == '*' or op == 'X':
        res = num1 * num2
    else:
        print("Invalid opertator. Use only (+, -, /, *).")
        return
    print("Result : " + str(res))
    save_history(user_input, res)

def main():
    print("==== SIMPLE CALCULATOR ====")

    while True:
        user_input = input("Enter The Expression OR Command (history, clear or exit) : ")

        if user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        elif user_input == 'exit':
            print("Thank You!")
            break
        else:
            calculate(user_input)

main()