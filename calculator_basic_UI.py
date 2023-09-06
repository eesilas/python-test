import tkinter as tk

# define the calculator function
def calculator():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operator = operator_var.get()

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = 'Invalid operator'

    result_label.config(text='Result: ' + str(result))

# create the GUI
root = tk.Tk()
root.title('Calculator')

# create the input fields and labels
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)
entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)
operator_var = tk.StringVar(value='+')
operator_label = tk.Label(root, text='Operator:')
operator_label.grid(row=0, column=1, padx=5, pady=5)
operator_menu = tk.OptionMenu(root, operator_var, '+', '-', '*', '/')
operator_menu.grid(row=1, column=1, padx=5, pady=5)

# create the calculate button
calculate_button = tk.Button(root, text='Calculate', command=calculator)
calculate_button.grid(row=2, column=1, padx=5, pady=5)

# create the result label
result_label = tk.Label(root, text='Result: ')
result_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# start the GUI
root.mainloop()
