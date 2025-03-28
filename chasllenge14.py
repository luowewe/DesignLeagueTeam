import turtle  # Import the turtle module to use its graphics functionality

# Define the draw_spiral function that draws an Archimedean spiral
def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    """Draws an Archimedian spiral starting at the origin.

    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosely coiled the spiral is (larger is looser)

    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0  # Initialize the angle (theta) to 0.0

    # Loop to draw 'n' line segments
    for i in range(n):
        t.fd(length)  # Move the turtle forward by the specified length

        # Calculate the change in angle (dtheta) based on the formula
        dtheta = 1 / (a + b * theta)

        # Turn the turtle left by the calculated angle (dtheta)
        t.lt(dtheta)

        # Update the angle (theta) for the next iteration
        theta += dtheta


# Create a turtle object named bob
bob = turtle.Turtle()

# Create a screen object to control the turtle window
screen = turtle.Screen()

# Set the background color of the turtle graphics window to white
screen.bgcolor("white")

# Call the draw_spiral function with the turtle object 'bob' and 1000 line segments
draw_spiral(bob, n=1000)

# No need for turtle.mainloop() in Trinket, as the window closes automatically when the program finishes
