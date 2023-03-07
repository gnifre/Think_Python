import turtle


# This is a sample Python script  to test the type function.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def test_turtle():
    # Use a breakpoint in the code line below to debug your script.
    # Back to 1988!
    little_turtle = turtle.Turtle()
    print(little_turtle)
    paint_square(little_turtle)

    # Another using for
    turtle.home()
    for i in range(4):
        little_turtle.rt(90)
        little_turtle.fd(200)

    turtle.mainloop()

def paint_square(little_turtle):
    little_turtle.fd(100)
    little_turtle.lt(90)
    little_turtle.fd(100)
    little_turtle.lt(90)
    little_turtle.fd(100)
    little_turtle.lt(90)
    little_turtle.fd(100)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_turtle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
