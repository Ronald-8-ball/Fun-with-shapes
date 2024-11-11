import turtle
turtle.Screen().bgcolor("pink")
# Start a work Screen
board = turtle.Screen()
# Define a Turtle Instance
board = turtle.Turtle()
# executing loop 6 times for 6 sides
for i in range(6):
    # Move forward by 90 units
    board.forward(90)
    # Turn left the turtle by 300 degrees
    board.left(300)
turtle.done()