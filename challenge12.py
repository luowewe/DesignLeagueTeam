import math  # Import the math module for mathematical operations
import turtle  # Import the turtle module for drawing

# Function to draw a pie shape and move to the right
def draw_pie(t, n, r):
    """Draws a pie, then moves into position to the right."""
    polypie(t, n, r)  # Draw the pie using the polypie function
    t.pu()  # Lift the pen to move without drawing
    t.fd(r * 2 + 10)  # Move forward to the next position
    t.pd()  # Put the pen down to start drawing again

# Function to draw a pie with n radial segments
def polypie(t, n, r):
    """Draws a pie divided into radial segments."""
    angle = 360.0 / n  # Calculate the angle for each segment
    for _ in range(n):  # Repeat for each segment
        isosceles(t, r, angle / 2)  # Draw an isosceles triangle for each segment
        t.lt(angle)  # Rotate left to position for the next segment

# Function to draw an isosceles triangle
def isosceles(t, r, angle):
    """Draws an isosceles triangle."""
    y = r * math.sin(math.radians(angle))  # Calculate the height of the triangle
    t.rt(angle)  # Rotate right to position for drawing the first side
    t.fd(r)  # Draw the first side
    t.lt(90 + angle)  # Rotate to draw the base
    t.fd(2 * y)  # Draw the base
    t.lt(90 + angle)  # Rotate to position for the second side
    t.fd(r)  # Draw the second side
    t.lt(180 - angle)  # Rotate back to the original position

# Create a turtle named pepito
pepito = turtle.Turtle()
pepito.speed(0)  # Set the turtle speed to the fastest

pepito.pu()  # Lift the pen to move without drawing
pepito.bk(130)  # Move backward to the starting position
pepito.pd()  # Put the pen down to start drawing

size = 40  # Set the size of the pie segments

# Draw multiple pie shapes with different segment counts
draw_pie(pepito, 5, size)  # Draw a pie with 5 segments
draw_pie(pepito, 6, size)  # Draw a pie with 6 segments
draw_pie(pepito, 7, size)  # Draw a pie with 7 segments
draw_pie(pepito, 8, size)  # Draw a pie with 8 segments

pepito.hideturtle()  # Hide the turtle after drawing is complete
turtle.done()  # Finish the turtle graphics execution
