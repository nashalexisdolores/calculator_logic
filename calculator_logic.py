class CalculatorParent:
    def __init__(self):
        self.app_title = "CMPE-103 Calculator App"

    def execute_math(self, operation, n1, n2):
        if operation == "Addition":
            return n1 + n2
        elif operation == "Subtraction":
            return n1 - n2
        elif operation == "Multiplication":
            return n1 * n2
        elif operation == "Division":
            if n2 == 0:
                raise ZeroDivisionError("Math Error: Cannot divide by zero!")
            return n1 / n2

class CalculatorChild(CalculatorParent):
    def __init__(self):
        super().__init__()

    def process_calculation(self, op, val1, val2):
        try:
            num1 = float(val1)
            num2 = float(val2)
            return self.execute_math(op, num1, num2)
        except ValueError:
            raise ValueError("Input Error: Please enter valid numbers.")