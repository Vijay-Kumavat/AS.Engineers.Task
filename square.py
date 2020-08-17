import turtle

# default square
print()
print('"Your Default square size is : 15 px"')
print()
print("Do you want to change square size ?")
turtle.bgcolor("gray")
turtle.color("black","olive")
turtle.pensize(5)

turtle.begin_fill()
turtle.shape("square") # create the square using shape method.
turtle.shapesize(15) #shape size.
turtle.end_fill()

print()

b = int(input("So, enter the value for square in px : ")) # Enter the any interger value for area of square.

turtle.reset() #reset the python turtle graphic

print()

print('"Thank you, you can check your square in python turtle graphic."')

d = b*b # area of square

window = turtle.Screen() # Pop up a new window using turtle screen method.

# resizeable square
turtle.bgcolor("gray")
turtle.color("black","olive")
turtle.pensize(5)

turtle.begin_fill()
turtle.shape("square") # create the square using shape method.
turtle.shapesize(d) #shape size.
turtle.end_fill()

window.exitonclick() # when you click the GUI page, then python turtle graphic is closed.