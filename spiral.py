import turtle

def draw_rainbow_spiral():
    # window = wn
    wn = turtle.Screen()
    wn.bgcolor("lightblue")

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

if __name__ == "__main__":
    draw_spiral()