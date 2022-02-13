from random import choice as ch

# block text is usually placed at the start i guess
title_banner = """
.   ,  ,.  ,---. .  .  ,-.  ,     ,.  .   , ,--. ,-.  
|\ /| /  \   |   |  | (   ` |    /  \  \ /  |    |  ) 
| V | |--|   |   |--|  `-.  |    |--|   Y   |-   |-<  
|   | |  |   |   |  | .   ) |    |  |   |   |    |  \ 
'   ' '  '   '   '  '  `-'  `--' '  '   '   `--' '  '
"""

help = """
    To get a high score, answer each question correctly!
    You can pick between 4 modes, as well as adjust the number
    of questions and difficulty in Options.
"""

mode = {1: "+", 2: "-", 3: "x", 4: "/"}


def line():
    """Prints a line for seperating menus"""
    print("-" * 66)


def input_int(min_num: int = -9999999, max_num: int = 9999999):
    """Returns the first integer user input between min_num and max_num"""
    while True:
        try:
            num = int(input(">> "))
            if (num < min_num) or (num > max_num):
                print("Error! Please enter a valid number.")
                continue
            return num
        except ValueError:
            print("Error! Please enter a valid number.")


class GameManager:
    """Class for handling menus and parameters of the GameLoop"""

    # default params when program starts, 11 is used so 10 can be included in qs
    parameters = {"num_q": 10, "num1": (2, 11), "num2": (2, 11)}

    def display(self):
        """Prints the main menu and waits for input."""
        print(title_banner)
        print("[1] Play")
        print("[2] Help")
        print("[3] Options")
        print("[4] Exit")

        return input_int(1, 4)

    def display_mode(self):
        """Prints the mode menu and waits for input."""
        print("Choose your game mode:")
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")

        return input_int(1, 4)

    def display_end_screen(self):
        """Prints the end screen after the game has ended."""
        line()
        print("Congratulations, you've finished the game!\n")
        print("Out of", Question.answered, "questions, ", end="")
        print("you have answered", Question.answered_correct, "correctly.")

    def display_help(self):
        """Prints help."""
        print(help)

    def display_options(self):
        """Prints the options and lets the user adjust game parameters."""
        print("Options:\n")
        print("[1] Number of Questions")
        print("[2] Difficulty")

        selection = input_int(1, 2)

        if selection == 1:
            print("How many questions do you want to answer?")
            GameManager.parameters["num_q"] = input_int(1, 1000)

        elif selection == 2:
            # felt necessary to define ranges for both nums bc of certain use cases
            print("Input the smallest number for the first number:")
            small_num1 = input_int(1, 1000000)
            print("Input the largest number for the first number:")
            big_num1 = input_int(small_num1 + 1, 1000001)
            print("Input the smallest number for the second number:")
            small_num2 = input_int(1, 1000000)
            print("Input the largest number for the second number:")
            big_num2 = input_int(small_num1 + 1, 1000001)

            # add 1 to big_num so big_num is included in the range of numbers for q
            GameManager.parameters["num1"] = (small_num1, big_num1 + 1)
            GameManager.parameters["num2"] = (small_num2, big_num2 + 1)

    def display_exit(self):
        """Prints the ending tagline."""
        print("Thank you for playing. See you next time!")
        line()

    def reset_game(self):
        """Clears the necessary vars after finishing a game."""
        Question.answered = 0
        Question.answered_correct = 0


class GameLoop:
    """Class for handling the flow of the game, such as asking questions."""

    def __init__(self, curr_mode: str):

        # using the current parameters, generates the qs and stores them
        num1 = range(*GameManager.parameters["num1"])
        num2 = range(*GameManager.parameters["num2"])
        q_range = range(GameManager.parameters["num_q"])
        op = mode[curr_mode]

        # no instance vars besides self.q_list bc it seems unnecessary for now
        self.q_list = [Question(ch(num1), ch(num2), op) for q in q_range]

    def ask_q(self):
        """Executes the general flow of the game."""
        current_q = self.q_list[Question.answered]

        line()
        current_q.display()
        answer = input_int()
        current_q.check(answer)


class Question:
    """Class for the questions used in the game."""

    answered: int = 0
    answered_correct: int = 0

    def __init__(self, num1: int, num2: int, operation: str):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

        # this part generates the questions, might be better to seperate this
        if operation == "+":
            self.correct_answer = num1 + num2
        elif operation == "-":
            self.correct_answer = num1 - num2
        elif operation == "x":
            self.correct_answer = num1 * num2
        elif operation == "/":
            # this one is different to make difficulty more interesting
            self.correct_answer = num1
            self.num1 = num1 * num2
        else:
            # make sure to add here if you want more modes
            raise TypeError

        # unnecessary (for now) bc all possible results are ints anyway
        # self.correct_answer = int(self.correct_answer)
        self.answered += 1

    def display(self):
        """Displays the current question and score."""
        print("Question", Question.answered + 1, end="\t" * 5)
        print("Score: {}/{}".format(Question.answered_correct, Question.answered))
        print(end="\t\t\t   ")

        # for different modes, you may want to create a different display
        print(self.num1, self.operation, self.num2, "= ?")
        return None

    def check(self, answer: int):
        """Checks the given answer and adjusts game variables accordingly."""
        Question.answered += 1
        if answer != self.correct_answer:
            print("Wrong! The correct answer is", self.correct_answer)
        else:
            print("Correct!")
            Question.answered_correct += 1

        return None


menu = GameManager()

while True:

    line()
    option = menu.display()
    line()

    if option == 1:
        new_mode = menu.display_mode()
        new_game = GameLoop(new_mode)

        while Question.answered < GameManager.parameters["num_q"]:
            new_game.ask_q()

        menu.display_end_screen()
        menu.reset_game()

    elif option == 2:
        menu.display_help()

    elif option == 3:
        menu.display_options()

    elif option == 4:
        menu.display_exit()
        break
