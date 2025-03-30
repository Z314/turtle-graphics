# This program draws a design using repeated circles.
import turtle

turtle.colormode(255)

# Named constants
NUM_CIRCLES = 36 # Number of circles to draw
RADIUS = 100 # Radius of each circle
ANGLE = 10 # Angle to turn
ANIMATION_SPEED = 0 # Animation speed

# Set the animation speed.
turtle.speed(ANIMATION_SPEED)

# Draw 36 circles, with the turtle tilted
# by 10 degrees after each circle is drawn.
for x in range(NUM_CIRCLES):
    turtle.pencolor(x*5, x*3, x*5)  # set the draw colour
    turtle.circle(RADIUS) # draw circle with size RADIUS
    turtle.left(ANGLE) # turn the turtle left by ANGLE

# make graphics window stay open
turtle.done()
