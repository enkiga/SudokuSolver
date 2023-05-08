from tkinter import *
from sudoku_soln import solve

root = Tk()
root.title("Sudoku Solver GUI")
root.geometry("500x500")

# Create a label widget
label = Label(root, text="Enter the Sudoku Puzzle Below")
label.grid(row=0, column=0, columnspan=10)

# error label
errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

# solved label
solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

# Create an empty dictionary to store the entries
entries = {}


# Create a register to validate the input
def validate_input(P):
    out = (P.isdigit() or P == "") and len(P) < 2
    return out


reg = root.register(validate_input)


# Create a sudoku grid
# Create the 3*3 grid first
def draw_grid(row, col, bg_color):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bg_color, justify="center", validate="key", validatecommand=(reg, '%P'))
            e.grid(row=row + i + 1, column=col + j + 1, sticky=NSEW, padx=1, pady=1, ipadx=1, ipady=5)
            entries[(row + i + 1, col + j + 1)] = e


# Create the 9*9 grid
def draw_sudoku():
    color = "light grey"
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw_grid(rowNo, colNo, color)
            if color == "light grey":
                color = "light blue"
            else:
                color = "light grey"


def clear_values():
    errLabel.config(text="")
    solvedLabel.config(text="")
    for row in range(2, 11):
        for col in range(1, 10):
            entries[(row, col)].delete(0, END)


def get_values():
    # create empty board for each value
    board = []
    errLabel.config(text="")
    solvedLabel.config(text="")
    for row in range(2, 11):
        row_list = []
        for col in range(1, 10):
            value = entries[(row, col)].get()
            if value == "":
                row_list.append(0)
            else:
                row_list.append(int(value))
        board.append(row_list)
    update_value(board)


# Create Buttons
# Get Values Button
btn = Button(root, command=get_values, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)

# Clear Values Button
btn = Button(root, command=clear_values, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5, pady=20)


# Call the solver
def update_value(s):
    sol = solve(s)
    if sol:
        for row in range(2, 11):
            for col in range(1, 10):
                entries[(row, col)].delete(0, END)
                entries[(row, col)].insert(0, s[row - 2][col - 1])
        solvedLabel.config(text="Solved!")
    else:
        errLabel.config(text="No Solution Found")


draw_sudoku()
root.mainloop()
