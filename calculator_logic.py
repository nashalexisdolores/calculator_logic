import sys

class CalculatorBase:
    """Base class for shared calculator properties."""
    def __init__(self):
        self.operations_menu = {
            '1': 'Addition',
            '2': 'Subtraction',
            '3': 'Multiplication',
            '4': 'Division'
        }
        
        def get_validated_number(self, prompt):
        """Ensures input is numeric using try-except."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid Input: Please enter a numeric value.")