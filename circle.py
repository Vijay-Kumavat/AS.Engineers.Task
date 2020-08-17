import turtle

# default circle
print()
print("Your Default circle size is : 100 px")
print()
print("Do you want to change circle size ?")
turtle.bgcolor("gray")
turtle.color("black","olive")
turtle.pensize(5)

turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

print()

a = float(input("So, enter the Vaule for Circle in px : ")) # Enter the any interger value for area of circle.

turtle.reset() #reset the python turtle graphic

print()

print('"Thank you, your changeable circle is in python turtle graphic."')

c=3.14*a*a # area of circle

window = turtle.Screen() # Pop up a new window using turtle screen method.

# turtle.circle(a)  # # create the circle using turtle method.

# resizeable circle
turtle.bgcolor("gray")
turtle.color("black","olive")
turtle.pensize(5)

turtle.begin_fill()
turtle.circle(c)
turtle.end_fill()

window.exitonclick() # when you click the GUI page, then python turtle graphic is closed.