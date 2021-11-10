from random import randint

class Question:

    question_num = 0
    question_right = 0

    def __init__(self, num1: int, num2: int, operation: str):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

        if operation == "+":
            self.correct = num1 + num2
        elif operation == "-":
            self.correct = num1 - num2
        elif operation == "x":
            self.correct = num1 * num2
        elif operation == "/":
            self.correct = num1
            self.num1 = num1 * num2
        else:
            self.correct = None

        self.correct = int(self.correct)
        self.question_num += 1
    
    def show(self):
        print("{} {} {} = ?".format(
            self.num1, self.operation, self.num2))
        return None
    
    def check(self, answer: int):
        if type(answer) != int:
            print("Error! Please enter a valid answer.")
            return -1
        elif answer != self.correct:
            print("Wrong! The correct answer is {ans}.".format(self.correct))
            Question.question_num += 1
            return 0
        else:
            print("Correct!".format(self.correct))
            Question.question_right += 1
            Question.question_num += 1
            return 1

# questions = [Question(randint(1,10), randint(1,10), "+") for i in range(10)]
# for q in questions:
#     q.show()