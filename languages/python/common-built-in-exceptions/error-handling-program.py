# NameError example
try:
    name = input("What is your name? ")
    greeting()
except NameError:
    print(
        "Oof! Looks like I forgot to define the 'greeting' function"
        + "\n"
        + f"Hope you're having a great day {name}!"
    )

# AttributeError example
try:
    animal = input("What's your favorite animal? ")
    print(f"{animal} has {animal.eat()}.")
except AttributeError:
    print(
        "Uh oh, looks like I can't use the 'eat' function on that. Better try other animal."
    )

# ImportError example
try:
    module_name = input("Type in an awesome AI superpower to import to this chat: ")
    import non_existent_module
except ImportError:
    print(
        f"Whoops! Looks like I couldn't import the module {module_name}. Better check the spelling."
    )

# ValueError example
try:
    age = int(input("How old are you? "))
    if age < 0:
        raise ValueError("Sorry, age can't be negative.")
except ValueError as e:
    print(f"Oops! {e}")

# TypeError example
try:
    num = input("Give me a number: ")
    print(f"Two divided by {num} is {2 / num}.")
except TypeError:
    print(f"Uh?1 Looks like I can't divide {num}. What are you doing?!")

# IndexError example
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
numbers = [num1, num2, num3]
try:
    print(f"The fourth number is {numbers[3]}.")
except IndexError:
    print("Hey! That list doesn't have a fourth element.")

# KeyboardInterrupt example
try:
    print(
        "I'm going to keep asking you to type something until you give up and press Ctrl-C!"
    )
    while True:
        input("Type something: ")
except KeyboardInterrupt:
    print("Ha! I knew you couldn't keep up forever. You win this round, human.")
