"""Recursion course from Robin Andrews on LinkedIn Learning
   :author: JR Steiner
   :date: 28/08/2022
"""
# import turtle
from functools import wraps
import sys
import trace

MAX_LENGTH = 2500
INCREMENT = 0.2


def draw_spiral(a_turtle, line_length):
    if line_length > MAX_LENGTH:
        return
    a_turtle.forward(line_length)
    a_turtle.right(22.5)
    draw_spiral(a_turtle, line_length + INCREMENT)


def factorial_iterative(n: int) -> int:
    _temp: int = 1
    while n >= 1:
        _temp *= n
        n -= 1
    return _temp


def factorial_recursive(n: int) -> int:
    """calculate the factorial of an integer number using recursion.
    :Inputs:
    :n [int]: number which the factorial will be calculated
    :returns:
    the factorial of n
    """
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def main():
    # charlie = turtle.Turtle(shape="turtle")
    # charlie.pensize(5)
    # charlie.color("brown")
    # draw_spiral(charlie, 10)
    # turtle.done()

    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(2) == 2
    assert factorial_recursive(3) == 6
    assert factorial_recursive(4) == 24
    assert factorial_recursive(5) == 120
    assert factorial_recursive(-5) == 1

    factorial = trace(factorial_recursive)
    factorial(5)


if __name__ == "__main__":
    main()
