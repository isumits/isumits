import turtle
import random
import time

delay=0.1
score=0
heighestscore=0

#snakebodies
bodies=[]

#Getting a screen | canvas
s=turtle.Screen()
s.title("Snake game")
s.bgcolor("gray")
s.setup(width=600,height=600)

#create snake head
head=turtle.Turtle()
head.speed(0)
head.color("white")
head.shape("circle")
head.fillcolor("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.turtle()
food.speed(0)
food.color("green")
food.shape("square")
food.fillcolor("red")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#score
sb=turtle.Turtle()
sb.shape("square")
