# Project-18---Hirst-Painting

This is a beginner-to-intermediate Python project built as part of my 100 Days of Code challenge.

The goal of this project is to recreate a Damien Hirst–style dot painting using Python’s Turtle graphics, randomization, and color extraction from an image.

**Project Overview**

The Hirst Painting project generates a grid of colorful dots by:

Extracting colors from an image

Randomly selecting colors for each dot

Drawing a structured dot grid using Turtle graphics

Creating a visually appealing generative artwork

The final result is a programmatically generated painting inspired by real-world art.

**Why this project exists**

This project was created to explore creative coding and understand how programming can be used to generate visual art.

It also helped reinforce how loops, randomness, and coordinate systems work together in graphical applications.

**What I learned**

How to extract color data from images using external libraries

How RGB color values work in graphical environments

How to use Turtle graphics for drawing shapes and patterns

How nested loops control two-dimensional layouts

How randomness can be used to create unique outputs every run

How to position elements precisely using x/y coordinates

**How the code works (step-by-step)**

Extract RGB colors from an image using the colorgram library.

Store extracted colors as RGB tuples in a list.

Set up a Turtle graphics screen with RGB color support.

Position the turtle at a starting coordinate.

Use nested loops to draw a grid of dots.

Randomly select a color for each dot from the extracted palette.

Display the final artwork until the user clicks the screen.

**Project File Structure**

├── main.py          # Drawing logic and program flow

├── image.jpeg       # Reference image for color extraction

**Example Output**

A 13×13 grid of evenly spaced colored dots,

each randomly selected from the extracted color palette,

creating a unique Hirst-style painting every time the program runs.

