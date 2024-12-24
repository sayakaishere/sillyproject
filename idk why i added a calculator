import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Awiokwawok")
        master.geometry("400x600")
        master.configure(bg="#000000")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        # Display
        self.display = tk.Entry(master, textvariable=self.result_var, font=("Helvetica", 48), bd=0, insertwidth=2, width=14, borderwidth=0, justify='right', bg="#FFFFFF")
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(master, text=button, padx=20, pady=20, font=("Helvetica", 24), command=action, bg="#F0F0F0", fg="#000000", activebackground="#D0D0D0", borderwidth=0, highlightthickness=0).grid(row=row_val, column=col_val, sticky="nsew", padx=10, pady=10)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid weights for responsive design
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
        for i in range(1, 5):
            master.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("0")
        elif char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            if self.result_var.get() == "0":
                self.result_var.set(char)
            else:
                self.result_var.set(self.result_var.get() + char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
