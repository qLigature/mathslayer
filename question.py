from random import choice as ch

mode = {1: "+", 2: "-", 3: "x", 4: "/"}


def line():
    print("-" * 66)


def input_int():
    while True:
        try:
            num = int(input(">> "))
            return num
        except ValueError:
            print("Error! Please enter a valid number.")


class GameManager:

    configs = {"num_q": 10, "num1 diff": (2, 10), "num2 diff": (2, 10)}

    def display(self):
        print("\t\t\t M A T H S L A Y E R\n")
        print("[1] Play")
        print("[2] Help")
        print("[3] Options")
        print("[4] Exit")

        return input_int()

    def display_mode(self):
        line()
        print("Choose your game mode:")
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")

        return input_int()

    def end_screen(self):
        line()
        print("Congratulations, you've finished the game!\n")
        print("Out of", Question.answered, "questions, ", end="")
        print("you have answered", Question.answered_correct, "correctly.")

    def display_help(self):
        line()
        print(
            """
        To get a high score, answer each question correctly!
        You can pick between 4 modes, as well as adjust the number
        of questions and difficulty in Options.
        """
        )

    def display_options(self):
        pass

    def display_exit(self):
        print("Thank you for playing. See you next time!")
        line()


class GameLoop:
    def __init__(self, q_num: int, curr_mode: str):
        self.q_num = q_num
        self.curr_mode = curr_mode
        self.current_q = 0

        num1 = range(1, 10)  # difficulty
        num2 = range(1, 10)
        op = mode[self.curr_mode]
        q_range = range(self.q_num)

        self.q_list = [Question(ch(num1), ch(num2), op) for q in q_range]

    def ask_q(self):
        current_q = self.q_list[Question.answered]

        line()
        current_q.display()
        answer = input_int()
        current_q.check(answer)


class Question:

    answered: int = 0
    answered_correct: int = 0

    def __init__(self, num1: int, num2: int, operation: str):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

        if operation == "+":
            self.correct_answer = num1 + num2
        elif operation == "-":
            self.correct_answer = num1 - num2
        elif operation == "x":
            self.correct_answer = num1 * num2
        elif operation == "/":
            self.correct_answer = num1
            self.num1 = num1 * num2
        else:
            raise TypeError

        self.correct_answer = int(self.correct_answer)
        self.answered += 1

    def display(self):
        print("Question", Question.answered + 1, end="\t" * 5)
        print("Score: {}/{}".format(Question.answered_correct, Question.answered))
        print(end="\t\t\t   ")
        print(self.num1, self.operation, self.num2, "= ?")
        return None

    def check(self, answer: int):
        Question.answered += 1
        if answer != self.correct_answer:
            print("Wrong! The correct answer is", self.correct_answer)
        else:
            print("Correct!")
            Question.answered_correct += 1


menu = GameManager()
line()

while True:

    location = menu.display()

    if location == 1:
        new_game = GameLoop(10, menu.display_mode())

        while new_game.q_num > Question.answered:
            new_game.ask_q()

        menu.end_screen()

    elif location == 2:
        menu.display_help()

    elif location == 3:
        menu.display_options()

    elif location == 4:
        menu.display_exit()
        break

    Question.answered = 0
    Question.answered_correct = 0
    line()
