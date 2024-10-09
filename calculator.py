def calculate(expression):
    """
    in the try block every other mathematical operation is being verified 
    in this calculator project only mathematical operations like(+,-,*,/) is performed
    if any other operation is performered then error is handled
    """
    try:
        if '+' in expression:
            num1, num2 = expression.split('+')
            return float(num1) + float(num2)
        elif '-' in expression:
            num1, num2 = expression.split('-')
            return float(num1) - float(num2)
        elif '*' in expression:
            num1, num2 = expression.split('*')
            return float(num1) * float(num2)
        elif '/' in expression:
            num1, num2 = expression.split('/')
            if float(num2) == 0:
                return "Error: Division by zero is not allowed."
            return float(num1) / float(num2)
        else:
            return "Error: Invalid operator."
    except ValueError:
        return "Error: Invalid input."
        

"""
if any number is divised by zero it leads to infinity
so when number 2 is given 0 then it prints a error message
"""
    
def main():
    expression = input("Enter a Mathematical Expression: ")
    ans = calculate(expression)
    print(ans)

main()
