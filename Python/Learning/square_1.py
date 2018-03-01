import turtle



def draw():

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    offset = 0
    brad1 = 0
    while ( brad1 < 25 ):
        brad.right(offset)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        offset = offset + 25
        brad1 = brad1 + 1

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    square = 0
    while (square < 1):
        draw()
        square = square + 1
        


draw_square()      

