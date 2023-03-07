import turtle


# This is a sample Python script  to test the type function.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def test_turtle():
    # Use a breakpoint in the code line below to debug your script.
    # Back to 1988!
    little_turtle = turtle.Turtle()
    print(little_turtle)


    # Another using for
    turtle.home()
    polygon(current_turtle=little_turtle, steps=5, length=100)

    turtle.mainloop()

def paint_square(little_turtle):
    little_turtle.fd(100)
    little_turtle.lt(90)
    little_turtle.fd(100)
    little_turtle.lt(90)
    little_turtle.fd(100)
    little_turtle.lt(90)
    little_turtle.fd(100)

def polygon(current_turtle, steps, length):
    angle = 360/steps
    for i in range(steps):
        current_turtle.lt(angle)
        current_turtle.fd(length)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_turtle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
