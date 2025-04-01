import turtle  # Import the turtle module for drawing
import math  # Import the math module for calculations

# Function to draw an arc with a given radius and angle
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360  # Calculate the arc length
    n = int(arc_length / 3) + 1  # Determine the number of steps
    step_length = arc_length / n  # Calculate step length
    step_angle = float(angle) / n  # Calculate step angle
    
    for _ in range(n):  # Draw the arc in small steps
        t.fd(step_length)  # Move forward
        t.lt(step_angle)  # Turn left

# Function to draw a petal using two arcs
def petal(t, r, angle):
    for _ in range(2):  # Draw two arcs to form a petal
        arc(t, r, angle)  # Draw the first arc
        t.lt(180 - angle)  # Rotate to position for the second arc

# Function to draw a flower with n petals and a specified color
def flower(t, n, r, angle, hue):
    t.color(hue)  # Set the turtle's color
    for _ in range(n):  # Repeat for each petal
        petal(t, r, angle)  # Draw a petal
        t.lt(360.0 / n)  # Rotate to the position for the next petal

# Function to move the turtle without drawing
def move(t, length):
    t.pu()  # Lift the pen up
    t.fd(length)  # Move forward by specified length
    t.pd()  # Put the pen down

Pepito = turtle.Turtle()  # Create a turtle named Pepito
Pepito.speed(100)  # Set the turtle speed to the fastest

move(Pepito, -100)  # Move turtle to starting position
flower(Pepito, 7, 60.0, 60.0, "red")  # Draw a red flower with 7 petals

move(Pepito, 100)  # Move to a new position
flower(Pepito, 10, 40.0, 80.0, "blue")  # Draw a blue flower with 10 petals

move(Pepito, 100)  # Move to another position
flower(Pepito, 20, 140.0, 20.0, "purple")  # Draw a purple flower with 20 petals

move(Pepito, 50)  # Move to another position
flower(Pepito, 12, 20.0, 20.0, "green")  # Draw a green flower with 12 petals

Pepito.hideturtle()  # Hide the turtle after drawing is complete
turtle.done()  # Finish the turtle graphics program
