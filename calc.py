import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator By IH Efty")
        self.root.geometry("390x600")
        self.root.resizable(0, 0)

        self.expression = ""  

        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("(", 5, 0), (")", 5, 1), ("←", 5, 2), ("=", 5, 3)
        ]

        for (text, row, col) in buttons:
            tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button):
        if button == "=":
            self.calculate()
        elif button == "C":
            self.clear_input()
        elif button == "←":
            self.backspace()
        else:
            self.expression += str(button)
            self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except Exception as e:
            self.expression = "Error"
        self.update_display()

    def clear_input(self):
        self.expression = ""
        self.update_display()

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()