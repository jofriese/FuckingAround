
import turtle
#We're going to see if we can make a program that takes the user input of the number of sides of a shape
#And then we're going to see if we can have the shape drawn correctly
ShapeSides = int(input("How many sides does the shape that we're going to draw have? "))
for steps in range(ShapeSides):
	turtle.forward(500/ShapeSides)
	turtle.right(360/ShapeSides)
	for moresteps in range(ShapeSides):
		turtle.forward(250/ShapeSides)
		turtle.right(360/ShapeSides)