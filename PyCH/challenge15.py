import turtle  # Import the turtle module to use its graphics functionality

# Function to draw a Koch curve of a given length
def koch(t, length):
    if length < 3:  # If the length is smaller than 3, just draw a straight line
        t.forward(length)  # Move the turtle forward by the given length
    else:
        # Draw the first third of the Koch curve
        koch(t, length / 3)  # Recursively draw the first third of the curve
        
        # Turn left by 60 degrees
        t.left(60)  # Turn the turtle to the left by 60 degrees
        
        # Draw the second third of the Koch curve
        koch(t, length / 3)  # Recursively draw the second third of the curve
        
        # Turn right by 120 degrees
        t.right(120)  # Turn the turtle to the right by 120 degrees
        
        # Draw the third third of the Koch curve
        koch(t, length / 3)  # Recursively draw the third third of the curve
        
        # Turn left by 60 degrees
        t.left(60)  # Turn the turtle to the left by 60 degrees
        
        # Draw the final third of the Koch curve
        koch(t, length / 3)  # Recursively draw the final third of the curve

# Function to draw a snowflake by drawing three Koch curves
def snowflake(t, length):
    # Draw the first Koch curve
    for i in range(3):  # Loop 3 times to draw 3 sides of the snowflake
        koch(t, length)  # Draw a single Koch curve with the specified length
        t.right(120)  # Turn the turtle right by 120 degrees to form the snowflake shape

# Create a turtle object named pepito to draw
pepito = turtle.Turtle()  # Create a turtle object named 'pepito' to control the drawing

# Create a screen object to control the turtle window
screen = turtle.Screen()  # Create a screen object to control the window

# Set the background color of the turtle graphics window to white
screen.bgcolor("white")  # Set the background color of the window to white

# Set the speed of the turtle
pepito.speed(0)  # Set the turtle speed to the fastest setting

# Move the turtle to an appropriate starting position
pepito.penup()  # Lift the pen to move without drawing
pepito.goto(-150, 100)  # Move the turtle to position (-150, 100) on the screen
pepito.pendown()  # Put the pen down to start drawing

# Draw the snowflake with a side length of 300
snowflake(pepito, 300)  # Call the snowflake function to draw the snowflake with side length 300

# No need for turtle.mainloop() in Trinket, as the window closes automatically when the program finishes
