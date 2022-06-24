import math
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    radius = simpledialog.askinteger(title="Circle Calculator", prompt="Input a radius")
    choice = simpledialog.askstring(title="Circle Calculator", prompt="Would you like to calculate the area or the circumference of a circle?")

    if choice == "Area" or choice == "area":
        Area = math.pi * radius * radius
        messagebox.showinfo(title="Circle Calculator", message=Area)
    else:
        Circumference = 2 * math.pi * radius
        messagebox.showinfo(title="Circle Calculator", message=Circumference)

# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr 
