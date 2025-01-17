import turtle
import random


class Polygon:
    def __init__(self,sides,small):
        turtle.colormode(255)
        self.sides = sides
        self.small = small
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.border_size = random.randint(1, 10)


    def setup(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)


    def play(self):
        if self.small == "Yes":
            self.reduct_ratio = 0.6
            self.draw_polygon()
            for i in range(2):
                self.small_setup()
                self.small_create()

        elif self.small == "No":
            self.draw_polygon()


    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360/self.sides)
        turtle.penup()


    def small_setup(self):
        turtle.forward(self.size*(1-self.reduct_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-self.reduct_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size -= 24


    def small_create(self):
        self.draw_polygon()


pics = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))
if 1 <= pics <= 3 or 5 <= pics <= 7:
    for i in range(random.randint(20, 30)):
        if 1 <= pics <= 3:
            pic = Polygon(pics+2, "No")
        elif 5 <= pics <= 7:
            pic = Polygon(pics-2, "Yes")
        pic.setup()
        pic.play()
elif pics == 4 or pics == 8:
    for i in range(3):
        for j in range(random.randint(10, 15)):
            if pics == 4:
                pic = Polygon(i+3, "No")
                pic.setup()
                pic.play()
            elif pics == 8:
                pic = Polygon(i + 3, "Yes")
                pic.setup()
                pic.play()

turtle.done()