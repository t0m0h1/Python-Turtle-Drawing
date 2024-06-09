import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_house(origin):
    origin = (-50, -50) 
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    
    house = turtle.Turtle()
    house.color("black")
    house.pensize(3)
    house.goto(origin)
    
    # Draw the base of the house
    house.begin_fill()
    draw_square(house, 150)
    house.end_fill()

    # draw the roof
    house.penup()
    house.goto(0, 150)
    house.pendown()
    house.color("red")
    house.begin_fill()  # start filling with color
    draw_triangle(house, 150)
    house.end_fill()  # end filling with color
        
    wn.exitonclick()



draw_house()
