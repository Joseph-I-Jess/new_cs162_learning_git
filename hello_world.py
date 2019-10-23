"""Get input from user, print it back to the string."""


class Cat:
    """Class representing a cat..."""

    def __init__(self):
        """Initialize a default cat."""
        self.limbs = 4
        self.tail = "long"

    def __str__(self):
        """Return self represented as a string."""
        return f"THis cat has {self.limbs} limbs and has a {self.tail} tail."


def main():
    """Run my tests."""
    print("Hello?")

    """
    number = input("Please enter a number: ")
    print(f"You entered {number}")
    """

    my_cat = Cat()

    print(f"""my_cat: {my_cat}""")  # will call my_cat.__str__() for us...


if __name__ == "__main__":
    main()
