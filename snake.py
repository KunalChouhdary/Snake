import turtle
import time
import random


delay = 0.1

# SCORE
score = 0
high_score = 0


# BUILD SCREEN
window = turtle.Screen()
window.title("Snake Game by Kunal Choudhary")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0) # TURNS OFF SCREEN UPDATE

# BUILD SNAKE HEAD
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# BUILD SNAKE FOOD
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,200)

segments = []

# CREATE A PEN
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Calibri", 24, "normal"))

# FUNCTIONS
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# KEYBOARD BINDING
window.listen()
window.onkeypress(go_up,"w")
window.onkeypress(go_down,"s")
window.onkeypress(go_left,"a")
window.onkeypress(go_right,"d")

# Main game loop
while True:
    window.update()

    # CHECK FOR COLLISION WITH BORDER
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # HIDE THE SEGMENTS
        for segment in segments:
            segment.goto(1000,1000)

        # CLEAR SEGMENTS LIST
        segments.clear()

        # RESET SCORE
        score = 0
        # RESET DELAY
        delay = 0.1

        # RESET SCORE
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Calibri", 24, "normal"))



    # CHECK FOR COLLISION WITH FOOD
    if head.distance(food) < 20:
        # MOVE FOOD TO RANDOM SPOT
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)

        # ADD A SEGMENT
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("orange")
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)

        # SHORTEN DELAY
        delay -= 0.001

        # INCREASE THE SCORE
        score += 1
        if score > high_score:
            high_score == score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Calibri", 24, "normal"))


    # MOVE END SEGMENTS FIRST IN REVERSE ORDER
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # MOVE SEGMENT 0 TO WHERE HEAD IS
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    # CHECK FOR COLLISION WITH BODY
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            # RESET SCORE
            score = 0

            # RESET DELAY
            delay = 0.1

            # UPDATE SCORE
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Calibri", 24, "normal"))

    time.sleep(delay)


window.mainloop()


