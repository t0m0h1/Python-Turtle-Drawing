import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_rectangle(t, width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_circle(t, radius):
    t.circle(radius)


def draw_clouds(t, size):
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.color("white")
    t.begin_fill()
    draw_circle(t, 50)
    t.end_fill()

    t.penup()
    t.goto(-150, 100)
    t.pendown()
    t.color("white")
    t.begin_fill()
    draw_circle(t, 50)
    t.end_fill()

    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.color("white")
    t.begin_fill()
    draw_circle(t, 50)
    t.end_fill()

def draw_house(origin):
    origin = (-50, -50) 
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    
    house = turtle.Turtle()
    house.color("black")
    house.pensize(2)
    house.goto(origin)
    
    # Draw the base of the house
    house.begin_fill()
    draw_square(house, 150)
    house.end_fill()

    # draw the roof
    house.penup()
    house.goto(-50, 100)
    house.pendown()
    house.color("red")
    house.begin_fill()  # start filling with color
    draw_triangle(house, 150)
    house.end_fill()  # end filling with color

    # draw the door
    house.penup()
    house.goto(15, -50)
    house.pendown()
    house.color("brown")
    house.begin_fill()
    draw_rectangle(house, 25, 50)  # Updated: Draw a rectangle for the door
    house.end_fill()

    # draw the window
    house.penup()
    house.goto(-20, 30)
    house.pendown()
    house.color("blue")
    house.begin_fill()
    draw_square(house, 15)
    house.end_fill()

    # draw the window
    house.penup()
    house.goto(50, 30)
    house.pendown()
    house.color("blue")
    house.begin_fill()
    draw_square(house, 15)
    house.end_fill()

    # draw the chimney
    house.penup()
    house.goto(50, 120)
    house.pendown()
    house.color("black")
    house.begin_fill()
    draw_rectangle(house, 20, 30)
    house.end_fill()

    # draw the clouds
    draw_clouds(house, 40)

        
    wn.exitonclick()


if __name__ == "__main__":
    draw_house(origin=(-50, -50))
