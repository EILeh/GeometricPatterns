"""
Geometric patterns

Program asks the user to choose a geometric pattern (square, rectangle or
circle) and to input the dimensions. Then calculates and prints the district
and area to two decimal places. Program will end if user inputs q and prints
an error if user inputs something else than s,r, c or q.

Writer of the program: EILeh
"""

import math

def menu():
    """
    Print a menu for user to select which geometric pattern to use in
    calculations.
    """

    while True:

        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            square = square_details()

        elif answer == "r":
            rectangle = rectangle_details()

        elif answer == "c":
            circle = circle_details()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def square_conditions():
    """
    The conditions program goes through before printing circumference and area.
    """

    square_length = float(input("Enter the length of the square's side: "))

    while square_length <= 0:
        square_length = float(input("Enter the length of the square's side: "))

    else:
        return square_length


def square_details():
    """
    The formulas of the square, that are used, so the program can count
    circumference and area from the values that the user gave. Function also
    prints both, the circumference
    and the area of the square.
    """

    square_values = square_conditions()

    circumference = 4 * square_values
    print(f"The circumference is {circumference:.2f}")

    area = square_values * square_values
    print(f"The surface area is {area:.2f}")


def rectangle_first_side():
    """
    The information of the rectangles first side and the conditions that limits
    the values that user gives.
    """

    first_side = float(input("Enter the length of the rectangle's side 1: "))

    while first_side <= 0:
        first_side = float(input("Enter the length of "
                                 "the rectangle's side 1: "))

    else:
        return first_side


def rectangle_second_side():
    """
    The information of the rectangles second side and the conditions that limits
    the values that user gives.
    """

    second_side = float(input("Enter the length of the rectangle's side 2: "))

    while second_side <= 0:
        second_side = float(input("Enter the length of the rectangle's "
                                  "side 2: "))

    else:
        return second_side


def rectangle_details():
    """
    The formulas of the triangle, that are used, so the program can count
    circumference and area from the values that the user gave. Function calls
    both functions: rectangle_first_side and rectangle_second_side and prints
    both, the circumference and the area of the triangle, from the given values.
    """

    first = rectangle_first_side()

    second = rectangle_second_side()

    circumference = 2 * first + 2 * second
    print(f"The circumference is {circumference:.2f}")

    area = first * second
    print(f"The surface area is {area:.2f}")


def circle_conditions():
    """
    The conditions program goes through before printing circumference and area.
    """

    circle_radius = float(input("Enter the circle's radius: "))

    while circle_radius <= 0:
        circle_radius = float(input("Enter the length of the square's side: "))

    else:
        return circle_radius


def circle_details():
    """
    The formulas of the circle, that are used, so the program can count
    circumference and area from the values that the user gave. Function also
    prints both, the circumference
    and the area of the circle.
    """
    circle_values = circle_conditions()

    circumference = 2 * math.pi * circle_values

    print(f"The circumference is {circumference:.2f}")

    area = math.pi * circle_values ** 2

    print(f"The surface area is {area:.2f}")


def main():

    menu()

    print("Goodbye!")

if __name__ == "__main__":
    main()