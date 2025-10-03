def print_hello():
    print('hello')


def get_hello():
    return 'hello'


def ask_name_and_greet_user():
    name = input('What is your name? ')
    if name.lower() != 'thanos':
        print(f'Hi, {name.capitalize()}. Would you like to have a Hamburger?')
    else:
        print('Get out of here, Thanos! Nobody wants to play with you!')
def calculate_hypotenuse_length(a: float, b: float) -> float:
    """Return hypotenuse value."""
    return (a ** 2 + b ** 2) ** 0.5


def calculate_cathetus_length(a: float, c: float) -> float:
    """Return cathetus value."""
    return (c ** 2 - a ** 2) ** 0.5


if __name__ == '__main__':
    print_hello()  # should print "Hello"
    hello = get_hello()  # should return "Hello"
    print(hello)  # let's check the value of hello variable
    ask_name_and_greet_user()  # should ask name and greet
    print(calculate_hypotenuse_length(3, 4))  # should print 5.0
    print(calculate_cathetus_length(3, 5))  # should print 4.0