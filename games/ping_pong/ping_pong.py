import turtle

score_a = 0
score_b = 0

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Ping Pong")
wn.setup(width=800, height=600)
wn.tracer(0)

A = turtle.Turtle()
A.speed(0)
A.shape("square")
A.color("red")
A.shapesize(stretch_wid=5, stretch_len=1)
A.penup()
A.goto(-350, 0)

B = turtle.Turtle()
B.speed(0)
B.shape("square")
B.color("blue")
B.shapesize(stretch_wid=5, stretch_len=1)
B.penup()
B.goto(350, 0)

C = turtle.Turtle()
C.speed(0)
C.shape("square")
C.color("white")
C.penup()
C.goto(0, 0)
C.dx = 0.5
C.dy = 0.5

pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Player A : 0   Player B : 0",
          align="center", font=("times", 20, "bold"))


def A_up():
    y = A.ycor()
    y += 20
    A.sety(y)


def A_down():
    y = A.ycor()
    y -= 20
    A.sety(y)


def B_up():
    y = B.ycor()
    y += 20
    B.sety(y)


def B_down():
    y = B.ycor()
    y -= 20
    B.sety(y)


wn.listen()
wn.onkey(A_up, "w")
wn.onkey(A_down, "s")
wn.onkey(B_up, "Up")
wn.onkey(B_down, "Down")


while True:
    wn.update()

    C.setx(C.xcor() + C.dx)
    C.sety(C.ycor() + C.dy)

    if C.ycor() > 290:
        C.sety(290)
        C.dy *= -1

    if C.ycor() < -290:
        C.sety(-290)
        C.dy *= -1

    if C.xcor() > 390:
        C.goto(0, 0)
        C.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : " + str(score_a) + "  Player B : " +
                  str(score_b), align="center", font=("times", 20, "bold"))

    if C.xcor() < -390:
        C.goto(0, 0)
        C.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : " + str(score_a) + "  Player B : " +
                  str(score_b), align="center", font=("times", 20, "bold"))

    if C.xcor() > 340 and C.xcor() < 350 and C.ycor() < B.ycor() + 40 and C.ycor() > B.ycor() - 40:
        C.setx(340)
        C.dx *= -1

    if C.xcor() < -340 and C.xcor() > -350 and C.ycor() < A.ycor() + 40 and C.ycor() > A.ycor() - 40:
        C.setx(-340)
        C.dx *= -1
