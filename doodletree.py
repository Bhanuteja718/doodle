import turtle
import random

#setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree Generator - Bhanu Teja")

#Turtle setup
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()

def draw_tree(branch_length):
    if branch_length > 10:
        
        #Color transition (trunk → leaves)
        if branch_length < 30:
            t.color("lime")
        else:
            t.color("brown")

        t.pensize(branch_length / 10)
        t.forward(branch_length)

        angle = random.randint(15, 30)

        #Right branch
        t.right(angle)
        draw_tree(branch_length - random.randint(10, 20))

        #Left branch
        t.left(angle * 2)
        draw_tree(branch_length - random.randint(10, 20))

        #Back to original position
        t.right(angle)
        t.backward(branch_length)

#Start drawing
draw_tree(100)
turtle.done()