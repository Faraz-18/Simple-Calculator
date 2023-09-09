import tkinter

root = tkinter.Tk()
root.geometry("400x200")
root.title("Simple Calculator")

def calculate(operation):
    n1 = int(num1_entry.get())
    n2 = int(num2_entry.get())

    if operation == "add":
        result_label['text'] = f"Result: {n1 + n2}"
    elif operation == "subtract":
        result_label['text'] = f"Result: {n1 - n2}"

num1_label = tkinter.Label(root, text='Enter First Number: ')
num1_label.pack()
num1_entry = tkinter.Entry(root)
num1_entry.pack()

num2_label = tkinter.Label(root, text='Enter Second Number: ')
num2_label.pack()
num2_entry = tkinter.Entry(root)
num2_entry.pack()

add_btn = tkinter.Button(root, text='Add', command=lambda: calculate("add"), foreground="Green")
add_btn.pack()

subtract_btn = tkinter.Button(root, text='Subtract', command=lambda: calculate("subtract"), foreground="Red")
subtract_btn.pack()

result_label = tkinter.Label(root, text='Result: ')
result_label.pack()

root.mainloop()