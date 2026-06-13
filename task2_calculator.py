# Basic Calculator
# Handles +, -, *, / and a few extras

def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: Can't divide by zero"
        return a / b
    elif op == "%":
        if b == 0:
            return "Error: Can't mod by zero"
        return a % b
    elif op == "**":
        return a ** b
    else:
        return "Unknown operation"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Calculator ===")
    print("Operations: +  -  *  /  %  **\n")

    while True:
        a = get_number("First number: ")
        op = input("Operation: ").strip()
        b = get_number("Second number: ")

        result = calculate(a, op, b)

        # clean up display — show int if no decimal part
        if isinstance(result, float) and result == int(result):
            result = int(result)

        print(f"\n  {a} {op} {b} = {result}\n")

        again = input("Calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Done!")
            break

if __name__ == "__main__":
    main()
