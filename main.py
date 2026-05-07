import tkinter as tk
from tkinter import messagebox
from calculator_logic import CalculatorChild # Ensure this matches the logic file

class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.calculator = CalculatorChild()
        self.title(self.calculator.app_title)
        self.geometry("350x400")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Calculator Interface", font=("Helvetica", 14, "bold")).pack(pady=10)
        
        tk.Label(self, text="Number 1:").pack()
        self.entry_1 = tk.Entry(self)
        self.entry_1.pack(pady=5)

        tk.Label(self, text="Number 2:").pack()
        self.entry_2 = tk.Entry(self)
        self.entry_2.pack(pady=5)

        tk.Label(self, text="Select Operation:").pack(pady=5)
        self.op_var = tk.StringVar(value="Addition")
        ops = ["Addition", "Subtraction", "Multiplication", "Division"]
        self.option_menu = tk.OptionMenu(self, self.op_var, *ops)
        self.option_menu.pack(pady=5)

        self.btn_calculate = tk.Button(self, text="Calculate", command=self.handle_click)
        self.btn_calculate.pack(pady=20)

    def handle_click(self):
        try:
            result = self.calculator.process_calculation(
                self.op_var.get(),
                self.entry_1.get(),
                self.entry_2.get()
            )
            messagebox.showinfo("Result", f"The answer is: {result}")
            
            if not messagebox.askyesno("Try Again?", "Perform another calculation?"):
                self.destroy()
        except Exception as error:
            messagebox.showerror("Error", str(error))

if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()