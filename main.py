from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blueviolet")

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

def draw_shape():
    for shape in shapes:
        for _ in range(shapes[shape][1]):
            tim.forward(100)
            tim.rt(shapes[shape][0])
draw_shape()


# Main Section






screen = Screen()
screen.exitonclick()