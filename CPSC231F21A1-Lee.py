#CPSC231 Fall 2021 (Jonathan Hudson), Eugene Lee, T04-Zack Hassan, UCID 30137489, Oct. 1st 2021
#This code will obtain inputs from the user to produce a line and a circle. Then it will run a series of calculations to determine whether it intersects or not, then act accordingly.

#Importing the necessary libraries
import math
import turtle

#Setting up constants and variables for the screen setup
pointer = turtle.Turtle()
screen = turtle.getscreen()
SCREENWIDTH = 800
SCREENHEIGHT = 600
ORIGIN_X = 0
ORIGIN_Y = 0

#Setting up the screen to draw on and making the coordinate system (from the assignment outline)
screen.setup(SCREENWIDTH, SCREENHEIGHT, 0, 0)
screen.setworldcoordinates(ORIGIN_X, ORIGIN_Y, SCREENWIDTH, SCREENHEIGHT)

pointer.hideturtle()
screen.delay(delay=0)

#Drawing the X and Y axis through the middle point of the screen
pointer.penup()
pointer.goto(0,300)
pointer.pendown()
pointer.goto(800,300)
pointer.penup()
pointer.goto(400,0)
pointer.pendown()
pointer.goto(400,600)

#Acquiring the 7 necessary input from the user
x_center = int((input("Enter the X value of the center point of the circle: ")))
y_center = int((input("Enter the Y value of the center point of the circle: ")))
radius = float((input("Enter the value of the radius of the circle: ")))
x1_line = int((input("Enter the X value of the starting point of the line: ")))
y1_line = int((input("Enter the Y value of the starting point of the line: ")))
x2_line = int((input("Enter the X value of the end point of the line: ")))
y2_line = int((input("Enter the Y value of the end point of the line: ")))

#Fixing the offset of the y value of the circle's center
y_center2 = y_center - radius

#Creating the circle
pointer.penup()
pointer.goto(x_center,y_center2)
pointer.pendown()
pointer.pencolor("red")
pointer.circle(radius)

#Creating the line
starting_point = (x1_line, y1_line)
end_point = (x2_line, y2_line)
pointer.pencolor("blue")
pointer.penup()
pointer.goto(starting_point)
pointer.pendown()
pointer.goto(end_point)

#Setting up the 3 constants that will be used in the quadratic formula
A = (x2_line - x1_line)**2 + (y2_line - y1_line)**2
B = 2 * ((x1_line - x_center) * (x2_line - x1_line) + (y1_line - y_center) * (y2_line - y1_line))
C = (x1_line - x_center)**2 + (y1_line - y_center)**2 - radius**2

#Different variables we will need throughout
EPSILON = 0.75  #The amount of room for error that is allowed
intersect_circle_r = 5  #The radius of the small circle around the intersection
DISCRIMINANT = B**2 - (4 * A * C)
pointer.pencolor("green")
distance = math.sqrt((x1_line - x_center)**2 + (y1_line - y_center)**2)

#Calculating for the special case where the start and end point of the line are equal
if (x1_line == x2_line) and (y1_line == y2_line) :
    if (radius - EPSILON) <= distance <= (radius + EPSILON):
        #There is a single intersection
        pointer.penup()
        pointer.goto(x1_line, y1_line - intersect_circle_r)
        pointer.pendown()
        pointer.circle(intersect_circle_r)
    else:
        #There is no intersection
        pointer.penup()
        pointer.goto(400, 300)
        pointer.write("No Intersect!", align="center", font=("Arial", 16, "normal"))

#Setting up the 3 different cases of the discriminant
elif DISCRIMINANT < 0:
    #There is no intersection
    pointer.penup()
    pointer.goto(400, 300)
    pointer.write("No Intersect!", align="center", font=("Arial", 16, "normal"))
elif DISCRIMINANT == 0:
    alpha = (-B) / (2 * A)
    if 0 <= alpha <= 1:
        #There is a single intersection
        x_single_intersect = ((1 - alpha) * x1_line) + (alpha * x2_line)
        y_single_intersect = ((1 - alpha) * y1_line) + (alpha * y2_line)
        pointer.penup()
        pointer.goto(x_single_intersect, y_single_intersect - intersect_circle_r)
        pointer.pendown()
        pointer.circle(intersect_circle_r)
    else:
        pointer.penup()
        pointer.goto(400, 300)
        pointer.write("No Intersect!", align="center", font=("Arial", 16, "normal"))
elif DISCRIMINANT > 0:
    SQUARED = math.sqrt(DISCRIMINANT)
    alpha_add = (-B + SQUARED) / (2 * A)
    alpha_subtract = (-B - SQUARED) / (2 * A)
    num_of_intersections = 0
    if 0 <= alpha_add <= 1 :
        #There is an intersection
        x_double_intersect_1 = ((1 - alpha_add) * x1_line) + (alpha_add * x2_line)
        y_double_intersect_1 = ((1 - alpha_add) * y1_line) + (alpha_add * y2_line)
        pointer.penup()
        pointer.goto(x_double_intersect_1, y_double_intersect_1 - intersect_circle_r)
        pointer.pendown()
        pointer.circle(intersect_circle_r)
        num_of_intersections += 1
    if 0 <= alpha_subtract <= 1 :
        #There is an intersection
        x_double_intersect_2 = ((1 - alpha_subtract) * x1_line) + (alpha_subtract * x2_line)
        y_double_intersect_2 = ((1 - alpha_subtract) * y1_line) + (alpha_subtract * y2_line)
        pointer.penup()
        pointer.goto(x_double_intersect_2, y_double_intersect_2 - intersect_circle_r)
        pointer.pendown()
        pointer.circle(intersect_circle_r)
        num_of_intersections += 1
    if num_of_intersections == 0 :
        pointer.penup()
        pointer.goto(400, 300)
        pointer.write("No Intersect!", align="center", font=("Arial", 16, "normal"))

pointer.hideturtle()
screen.exitonclick()
