import turtle
#turtle
s = turtle.Screen()
t = turtle.Turtle()
u = turtle.Turtle()
r = turtle.Turtle()
l = turtle.Turtle()
e = turtle.Turtle()

#size settings
r.pensize(10)
u.pensize(10)
t.pensize(10)
l.pensize(10)
e.pensize(10)

#ini warna
s.bgcolor("#04103C")
t.pencolor("#3C6AA6")
u.pencolor("#61B0B7")
r.pencolor("#B8E3FF")
l.pencolor("#5791B3")
e.pencolor("#477977")

def huruf_s():
    t.forward(55)
    t.circle(50, 190)
    t.left(179)
    t.forward(5)
    t.circle(50, -190)
    t.left(180)
    t.forward(75)
    t.right(135)
    t.forward(40)
    t.right(45)
    t.forward(50)

def huruf_D():
    u.right(180)
    u.forward(50)
    u.right(45)
    u.forward(40)
    u.right(135)
    u.forward(75)
    u.circle(-100, 180)
    u.forward(30)
    u.right(90)
    u.forward(140)

def angka_9():
    l.left(180)
    l.forward(10)
    l.circle(-40, 180)
    l.forward(20)
    l.circle(-40, 120)
    l.right(10)
    l.forward(125)
def angka_3():
    r.forward(80)
    r.right(140)
    r.forward(60)
    r.left(140)
    r.forward(20)
    r.circle(-30,180)
    r.forward(60)
def angka_7():
    e.forward(80)
    e.right(120)
    e.forward(135)


#inti
t.penup()
t.goto(-210,-100)
t.pendown()
huruf_s()

l.penup()
l.goto(10,170)
l.pendown()
angka_9()

u.penup()
u.goto(170,80)
u.pendown()
huruf_D()

e.penup()
e.goto(-40,-100)
e.pendown()
angka_7()

r.penup()
r.goto(-40,50)
r.pendown()
angka_3()


s.exitonclick()
