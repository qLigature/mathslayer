from random import choice as ch

mode = {
    "addition": "+",
    "subtraction": "-",
    "multiplication": "x",
    "division": "/"
}

class Question:

    answered = 0
    answered_correct = 0

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
            self.correct_answer = None

        self.correct_answer = int(self.correct_answer)
        self.answered += 1
    
    def display(self):
        print("Question {}".format(
            Question.answered + 1), end = "\t\t\t\t\t\t")
        print("Score: {}/{}".format(
            Question.answered_correct, Question.answered))
        print(end = "\t\t\t   ")
        print("{} {} {} = ?".format(
            self.num1, self.operation, self.num2))
        return None
    
    def check(self, answer: int):
        try:
            answer = int(answer)
        except ValueError:
            print("Error! Please enter a valid answer.")
            return False

        Question.answered += 1
        if answer != self.correct_answer:
            print("Wrong! The correct answer is {}.".format(
                self.correct_answer))
            return True
        else:
            print("Correct!")
            Question.answered_correct += 1
            return True

class GameLoop:

    def __init__(self, q_num: int, curr_mode: str):
        self.q_num = q_num
        self.curr_mode = curr_mode
        self.current_q = 0

    def generate_q(self):
        num1 = range(1, 10)
        num2 = range(1, 10)
        op = mode[self.curr_mode]
        q_range = range(self.q_num)

        self.q_list = [Question(ch(num1), ch(num2), op) for q in q_range]
    
    def ask_question(self):
        question_done = False
        self.q_list[Question.answered].display()
        
        while question_done == False:
            answer = input(">> ")
            question_done = self.q_list[Question.answered].check(answer)
            
        print("---------------------------------", end = "")
        print("---------------------------------")

new_game = GameLoop(10, "division")
new_game.generate_q()
while new_game.q_num > Question.answered:
    new_game.ask_question()