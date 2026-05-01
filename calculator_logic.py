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