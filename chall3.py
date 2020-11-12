from turtle import *


def koch(l, n):
    if n <= 0:
        forward(l)
    else:
        koch(l/3, n-1)
        left(60)
        koch(l/3, n-1)
        right(120)
        koch(l/3, n-1)
        left(60)
        koch(l/3, n-1)


def snowflake(l, n):
    speed(100)
    fillcolor("blue")
    begin_fill()
    koch(l, n)
    right(120)
    koch(l, n)
    right(120)
    koch(l, n)
    end_fill()
