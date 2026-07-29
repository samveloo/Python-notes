import turtle

screen = turtle.Screen()
t = turtle.Turtle()

screen.bgcolor('#1E2021')
t.color('#ffffff')

def w():
    t.forward(10)

def s():
    t.backward(10)

def a():
    t.left(45)

def d():
    t.right(45)

screen.listen()

screen.onkeypress(w, "w")
screen.onkeypress(s, "s")
screen.onkeypress(a, "a")
screen.onkeypress(d, "d")

turtle.mainloop()