from tkinter import *
from math import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=13, font=('Verdana', 38), borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

global brackets
brackets = []


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def _button_clear():
    e.delete(0, END)
    global brackets
    brackets = []


def _button_equal():
    second_number = e.get()
    e.delete(0, END)

    # if bracket == "oBracket":
    #     brackets.append([f_num, math])
    #     print(brackets)

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    elif math == "subtraction":
        e.insert(0, f_num - float(second_number))

    elif math == "multiplication":
        e.insert(0, f_num * float(second_number))

    elif math == "division":
        e.insert(0, f_num / float(second_number))

    elif math == "square_root":
        e.insert(0, sqrt_sol)

    elif math == "x_square":
        e.insert(0, x_square_sol)

    elif math == "x_pow_y":
        e.insert(0, pow(f_num, float(second_number)))

    elif math == "euler":
        e.insert(0, 2.718281828459045)

    elif math == "comma":
        e.insert(0, second_number)

    global answer
    answer = e.get()


def _button_add():
    if e.get() == "e":
        first_number = 2.718281828459045
    else:
        first_number = e.get()

    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def _button_subtract():
    if e.get() == "e":
        first_number = 2.718281828459045
    else:
        first_number = e.get()

    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def _button_multiply():
    if e.get() == "e":
        first_number = 2.718281828459045
    else:
        first_number = e.get()

    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def _button_divide():
    if e.get() == "e":
        first_number = 2.718281828459045
    else:
        first_number = e.get()

    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def _button_answer():
    e.delete(0, END)
    e.insert(0, answer)


def _button_comma():
    global math
    math = "comma"
    if "." not in e.get():
        num = e.get()
        e.delete(0, END)
        e.insert(0, num + ".")


def _button_oBracket():
    brackets.append([f_num, math])
    print(brackets)


def _button_cBracket():
    second_numberInner = e.get()
    e.delete(0, END)

    global brackets

    global innerBrackets

    # solving inner ()

    if math == "addition":
        e.insert(0, f_num + float(second_numberInner))
        innerBrackets = e.get()

    elif math == "subtraction":
        e.insert(0, f_num - float(second_numberInner))
        innerBrackets = e.get()

    elif math == "multiplication":
        e.insert(0, f_num * float(second_numberInner))
        innerBrackets = e.get()

    elif math == "division":
        e.insert(0, f_num / float(second_numberInner))
        innerBrackets = e.get()

    elif math == "square_root":
        e.insert(0, sqrt_sol)
        innerBrackets = e.get()

    elif math == "x_square":
        e.insert(0, x_square_sol)
        innerBrackets = e.get()

    elif math == "x_pow_y":
        e.insert(0, pow(f_num, float(second_numberInner)))
        innerBrackets = e.get()

    elif math == "euler":
        e.insert(0, 2.718281828459045)
        innerBrackets = e.get()

    elif math == "comma":
        e.insert(0, second_numberInner)
        innerBrackets = e.get()

    # solving () and outer

    e.delete(0, END)

    if brackets[0][1] == "addition":
        e.insert(0, innerBrackets + float(brackets[0][0]))
        brackets = []

    elif brackets[0][1] == "subtraction":
        e.insert(0, innerBrackets - float(brackets[0][0]))

    elif brackets[0][1] == "multiplication":
        e.insert(0, float(innerBrackets) * float(brackets[0][0]))

    elif brackets[0][1] == "division":
        e.insert(0, innerBrackets / float(brackets[0][0]))


    global answer
    answer = e.get()


def _button_e():
    global math
    math = "euler"
    e.delete(0, END)
    e.insert(0, "e")


def _button_x_pow_y():
    if e.get() == "e":
        first_number = 2.718281828459045
    else:
        first_number = e.get()

    global f_num
    global math
    math = "x_pow_y"
    f_num = float(first_number)
    e.delete(0, END)


def _button_x_square():
    global math
    math = "x_square"

    if e.get() == "e":
        num = 2.718281828459045
    else:
        num = float(e.get())

    e.delete(0, END)
    global x_square_sol
    x_square_sol = num * num
    e.insert(0, x_square_sol)
    global answer
    answer = e.get()


def _button_sqrt():
    global math
    math = "square_root"

    if e.get() == "e":
        first_number = 2.718281828459045
    else:
        first_number = float(e.get())

    e.delete(0, END)
    global sqrt_sol
    sqrt_sol = sqrt(first_number)
    e.insert(0, sqrt_sol)
    global answer
    answer = e.get()


# Define buttons


button_1 = Button(root, text="1", padx=50, pady=20, bg="white", activebackground="grey", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=50, pady=20, bg="white", activebackground="grey", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=50, pady=20, bg="white", activebackground="grey", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=50, pady=20, bg="white", activebackground="grey", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=50, pady=20, bg="white", activebackground="grey", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=50, pady=20, bg="white", activebackground="grey", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=50, pady=20, bg="white", activebackground="grey", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=50, pady=20, bg="white", activebackground="grey", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=50, pady=20, bg="white", activebackground="grey", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=50, pady=20, bg="white", activebackground="grey", command=lambda: button_click(0))

button_add = Button(root, text="+", padx=50, pady=20, bg="#cccccc", command=_button_add)
button_subtract = Button(root, text="-", padx=50, bg="#cccccc", pady=20, command=_button_subtract)
button_multiply = Button(root, text="*", padx=50, pady=20, bg="#cccccc", command=_button_multiply)
button_divide = Button(root, text="÷", padx=50, pady=20, bg="#cccccc", command=_button_divide)

button_equal = Button(root, text="=", padx=50, pady=20, bg="#cae3d0", command=_button_equal)
button_clear = Button(root, text="C", padx=49, pady=20, bg="#b9b9c4", command=_button_clear)
button_answer = Button(root, text="Ans", padx=43, pady=20, bg="#cccccc", command=_button_answer)
button_comma = Button(root, text=",", padx=52, pady=20, bg="#cccccc", command=_button_comma)
button_oBracket = Button(root, text="(", padx=50, pady=20, bg="#cccccc", command=_button_oBracket)
button_cBracket = Button(root, text=")", padx=50, pady=20, bg="#cccccc", command=_button_cBracket)
button_e = Button(root, text="e", padx=50, pady=20, bg="#cccccc", command=_button_e)
button_x_pow_y = Button(root, text="x^y", padx=42, bg="#cccccc", pady=20, command=_button_x_pow_y)
button_x_square = Button(root, text="x^2", padx=42, pady=20, bg="#cccccc", command=_button_x_square)
button_sqrt = Button(root, text="√", padx=49, pady=20, bg="#cccccc", command=_button_sqrt)


# put buttons on the screen

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_add.grid(row=5, column=3)
button_clear.grid(row=1, column=3)

button_subtract.grid(row=4, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=2, column=3)

button_answer.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_comma.grid(row=6, column=2)
button_equal.grid(row=6, column=3)
button_oBracket.grid(row=2, column=0)
button_cBracket.grid(row=2, column=1)
button_e.grid(row=2, column=2)
button_x_pow_y.grid(row=1, column=0)
button_x_square.grid(row=1, column=1)
button_sqrt.grid(row=1, column=2)

root.mainloop()

