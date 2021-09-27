from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")


shapes = {
    "triangle": [120, 3],
    "square": [90, 4],
    "pentagon": [72, 5],
    "hexagon": [60, 6],
    "heptagon": [51, 7],
    "octagon": [45, 8],
    "nonagon": [40, 9],
    "decagon": [36, 10]
}

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

def draw_shape():
    for shape in shapes:
        for _ in range(shapes[shape][1]):
            tim.forward(100)
            tim.rt(shapes[shape][0])
        change_color()


draw_shape()


# Main Section

screen = Screen()
screen.exitonclick()