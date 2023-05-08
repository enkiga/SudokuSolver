- Creating a program that solves 9*9 Sudoku using BackTracking Algorithm

---

## Sudoku Solver Using Backtracking Algorithm

The given Python code uses the Tkinter library to create a GUI application for solving Sudoku puzzles. It imports the
solve function from the sudoku_soln module, which provides the algorithm for solving Sudoku puzzles.

The GUI displays a 9x9 grid of input fields, where the user can enter the puzzle to be solved. The input fields are
arranged in a 3x3 grid of 3x3 sub-grids. The GUI also includes two buttons: "Solve" and "Clear". The "Solve" button
calls the get_values function, which reads the values entered the input fields and passes them to the solve function
to find the solution. The "Clear" button calls the clear_values function, which clears all the input fields.

The validate_input function is used to validate the input entered each input field. It ensures that only digits are
entered and that the length of the input is less than 2.

The draw_sudoku function creates the 9x9 grid of input fields and assigns them to a dictionary called entries. The
update_value function updates the input fields with the solution obtained from the solve function.

Overall, the code creates a functional GUI application for solving Sudoku puzzles using the Tkinter library and the
solve function from the sudoku_soln module.

#### How to run the code

- Install Python: If you don't have Python installed on your system, you can download and install it from the official
  website: https://www.python.org/downloads/

- Install Tkinter: Tkinter is a standard GUI library for Python, and it's included in most Python installations.
  However,
  if you're using a version of Python that doesn't include Tkinter, you can install it using your system's package
  manager
  or by downloading it from the official website: https://tkdocs.com/tutorial/install.html

- Save the code: Save the code in a file with a .py extension, for example, "sudoku_solver.py".

- Run the code: Open your terminal or command prompt, navigate to the directory where the file is saved and run the
  following command:

```
python sudoku_solver.py
```

- Interact with the GUI: Once the code is running, you'll see a GUI window with a 9x9 Sudoku grid. Enter the numbers of
  the Sudoku puzzle you want to solve and click on the "Solve" button to solve the puzzle. Click on the "Clear" button
  to clear the grid and enter a new Sudoku puzzle.

#### Example

When you run the code the GUI will look like this:

![empty grid.png](images%2Fempty%20grid.png)

fill in the grid with the puzzle you want to solve and click on the "Solve" button:

![filled.PNG](images%2Ffilled.PNG)

The GUI will display the solution when you click solve:

![solved.PNG](images%2Fsolved.PNG)