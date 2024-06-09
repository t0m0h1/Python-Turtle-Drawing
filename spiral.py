import turtle

def draw_rainbow_spiral():
    # window = wn
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    wn.title("Rainbow Spiral")
    

    # spiral = turtle
    spiral = turtle.Turtle()
    spiral.pensize(2)
    spiral.speed(0)

    colours = ["red", "purple", "blue", "green", "yellow", "orange"]

    for i in range(360):
        spiral.pencolor(colours[i % 6])
        spiral.width(i / 100 + 1)
        spiral.forward(i)
        spiral.left(59)

    spiral.hideturtle()
    wn.exitonclick()


def draw_fractal():
    wn = turtle.Screen()
    wn.bgcolor("lightblue")

    fractal = turtle.Turtle()
    fractal.speed(0)
    fractal.color("black")
    fractal.pensize(2)

    def draw_fractal(length, depth):
        if depth == 0:
            fractal.forward(length)
        else:
            draw_fractal(length / 3, depth - 1)
            fractal.left(60)
            draw_fractal(length / 3, depth - 1)
            fractal.right(120)
            draw_fractal(length / 3, depth - 1)
            fractal.left(60)
            draw_fractal(length / 3, depth - 1)

    fractal.penup()
    fractal.goto(-150, 0)
    fractal.pendown()

    draw_fractal(300, 4)

    fractal.hideturtle()
    wn.exitonclick()

if __name__ == "__main__":
    draw_fractal()
