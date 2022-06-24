from tkinter import messagebox, simpledialog, Tk
import tkinter as tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    window_width = 600
    window_height = 600

    root = tk.Tk()

    canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
    canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
    tomatoColor = simpledialog.askstring(title="Tomato Color", prompt="What color tomato would you like?\nRed\nBlue\nPurple")

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
    if tomatoColor == "Red" or tomatoColor == "red":
        canvas.create_oval(75, 200, 400, 450, fill="red", outline="pink")
        canvas.create_oval(200, 200, 525, 450, fill="red", outline="pink")

        canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="green")
    elif tomatoColor == "Blue" or tomatoColor == "blue":
        canvas.create_oval(75, 200, 400, 450, fill="blue", outline="yellow")
        canvas.create_oval(200, 200, 525, 450, fill="blue", outline="yellow")

        canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="green")
    elif tomatoColor == "Purple" or tomatoColor == "purple":
        canvas.create_oval(75, 200, 400, 450, fill="purple", outline="orange")
        canvas.create_oval(200, 200, 525, 450, fill="purple", outline="orange")

        canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="green")
    else:
        messagebox.showerror(title="Outside of Scope", message="Wrong Color")
    root.mainloop()
