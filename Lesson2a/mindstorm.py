import turtle

def draw_square(turtle):
    i = 0
    while i < 4:
    
        turtle.forward(100)
        turtle.right(90)
    
        i = i + 1

def draw_circle_square():
    window = turtle.Screen()
    window.bgcolor("red")

    #create turtle
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("purple")
    brad.speed(2)

    for i in range(1,36):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()


#def draw_square():
#    window = turtle.Screen()
#    window.bgcolor("red")
    
#    brad = turtle.Turtle()
#    brad.shape("circle")
#    brad.color("purple")
#    brad.speed(2)

#    i = 0
#    while i < 4:
    
#        brad.forward(100)
#        brad.right(90)
    
#        i = i + 1

#    window.exitonclick()

#def draw_circle():
#    window = turtle.Screen()
#    window.bgcolor("yellow")

#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("blue")
#    angie.circle(100)

#    window.exitonclick()

#def draw_triangle():
#    window = turtle.Screen()
#    window.bgcolor("green")

#    ada = turtle.Turtle()
#    ada.shape("square")
#    ada.color("orange")

#    i = 0
#    while i < 3:
    
#        ada.forward(100)
#        ada.left(120)
    
#        i = i + 1

#    window.exitonclick()

#draw_square()
#draw_circle()
#draw_triangle()
draw_circle_square()
