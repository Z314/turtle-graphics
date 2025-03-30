# This program make a spiral triangle type pattern
# The % symbol in Python is the modulus operator. It returns the remainder when one number is divided by another.
# Note: print(10 % 3)  # 10 divided by 3 is 3 with remainder 1 → Output: 1
# Note: print(110 % 255)  # 110 divided by 255 is 0 with remainder 110 → Output: 110

import turtle # This is a the turtle graphics module (AKA library). We are going to use it in this program.

# Set up turtle
turtle.bgcolor("black")  # Set background color
turtle.speed(0)  # Fastest speed
turtle.colormode(255)  # Enable RGB color mode. Each value (RGB) must be between 0 and 255

# Draw a spiky spiral
for i in range(100):
    turtle.pencolor(i * 2 % 255, i * 3 % 255, i * 5 % 255)  # Dynamic RGB color, modulus operator (%) ensures value don't go above 255
    turtle.forward(i * 4)  # Increase step size
    turtle.right(123)  # Turn right specified angle

turtle.done()
