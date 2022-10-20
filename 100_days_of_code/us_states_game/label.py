from turtle import Turtle

FONT = ("Courier", 8, "normal")


class Label:

    def write_label(answer, x, y):
        new_label = Turtle()
        new_label.penup()
        new_label.hideturtle()
        new_label.write(arg=f"{answer}", font=FONT)
        new_label.goto(x, y)
