import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simple dialog.askinteger()
    radius = simpledialog.askinteger(title="Circle", prompt="What is the radius in pixels?")
    # Make a new turtle
    mathTurtle = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    mathTurtle.circle(radius)
    # Call the turtle .penup() method
    mathTurtle.penup()
    # Move your turtle to a new x,y position using .goto()
    mathTurtle.goto(x=0, y=0)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = math.pi * radius * radius
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    mathTurtle.write(arg="area = " + str(area), move=True, align='left', font=('Ariel', 8, 'normal'))
    # Hide your turtle
    mathTurtle.hideturtle()
    # Call turtle.done()
    turtle.done()
