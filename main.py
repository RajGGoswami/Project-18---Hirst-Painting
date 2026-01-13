# Day 18 – Hirst Painting
# This project recreates a Damien Hirst–style dot painting using Python graphics.
# The focus is on color extraction, randomness, loops, and graphical positioning.

import colorgram
from turtle import Turtle, Screen
import random

# Screen setup
# The Screen object controls the window where the Turtle graphics are displayed
screen = Screen()
screen.title("Raj's Hirst Painting GUI")
screen.colormode(255)  # Allows RGB colors in (0–255) format instead of default (0–1)

# This list will store RGB color tuples extracted from an image
rgb_colors = []

# Extract 30 colors from the reference image using the colorgram library
# This mimics the color palette style used in Hirst paintings
colors = colorgram.extract('image.jpeg', 30)

# Convert extracted colors into RGB tuples
# These tuples will later be randomly selected for each dot
for color in colors:
    cols = []
    cols.append(color.rgb.r)
    cols.append(color.rgb.g)
    cols.append(color.rgb.b)
    rgb_colors.append(tuple(cols))

# Create the Turtle that will draw the painting
tim = Turtle()
tim.color()
tim.hideturtle()        # Hides the turtle cursor for a cleaner visual
tim.speed("fast")       # Speeds up drawing to render the artwork quickly
tim.penup()             # Prevents lines from being drawn between dots

# Starting position for the dot grid (bottom-left corner)
x_cor = -350
y_cor = -350
tim.goto(x_cor, y_cor)

# Outer loop controls rows (vertical placement of dots)
for y_dots in range(13):

    # Inner loop controls columns (horizontal placement of dots)
    for x_dots in range(13):
        # Draw a dot with a random color from the extracted palette
        tim.dot(30, random.choice(rgb_colors))

        # Move right to the next dot position
        x_cor += 60
        tim.goto(x_cor, y_cor)

    # Move up to the next row
    y_cor += 60

    # Reset x-coordinate to the start of the row
    x_cor -= 60 * 13
    tim.goto(x_cor, y_cor)

# Keeps the window open until the user clicks
screen.exitonclick()
