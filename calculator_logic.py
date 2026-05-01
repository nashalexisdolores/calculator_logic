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

                def select_operation(self):
        """Displays menu and returns validated choice."""
        while True:
            print("\n--- Simple App Calculator ---")
            for key, value in self.operations_menu.items():
                print(f"{key}. {value}")
            choice = input("Select operation (1-4): ")
            if choice in self.operations_menu:
                return choice
            print("Invalid Selection: Choose 1-4.")

            class SimpleAppCalculator(CalculatorBase):
    """Derived class demonstrating inheritance."""
    def __init__(self):
        super().__init__()

        def perform_calculation(self, choice, num1, num2):
        """Performs calculation based on selection."""
        if choice == '1':
            return num1 + num2
        elif choice == '2':
            return num1 - num2
        elif choice == '3':
            return num1 * num2