import turtle

turtle.tracer(0)
turtle.hideturtle()

def surrounding(cor, size):
    x, y = cor
    return [(x - size, y + size),
            (x + size, y + size),
            (x - size, y - size),
            (x + size, y - size),
            (x - size, y),
            (x + size, y),
            (x, y + size),
            (x, y - size)]

def draw_square(cor, size, count):
    size /= 3
    count -= 1
    turtle.penup()
    turtle.goto(cor[0] - size / 2, cor[1] + size / 2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.end_fill()
    if count:
        func(surrounding(cor, size), size, count)

def func(cors, size, count):
    if len(cors) == 2:
        draw_square(cors, size, count)
    else:
        draw_square(cors[0], size, count)
        draw_square(cors[1], size, count)
        draw_square(cors[2], size, count)
        draw_square(cors[3], size, count)
        draw_square(cors[4], size, count)
        draw_square(cors[5], size, count)
        draw_square(cors[6], size, count)
        draw_square(cors[7], size, count)




func((0, 0), 600, 5)
turtle.update()
turtle.done()