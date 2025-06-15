
print("Welcome to the Quiz\n")

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question1 = Question(
    "1. What is the capital of Nigeria?\n"
    "a. Abuja\nb. Lagos\nc. Kano\nd. Ibadan\n",
    "a"
)

question2 = Question(
    "2. Which planet is known as the Red Planet?\n"
    "a. Earth\nb. Jupiter\nc. Mars\nd. Saturn\n",
    "c"
)

question3 = Question(
    "3. What is 5 * 6?\n"
    "a. 11\nb. 30\nc. 56\nd. 25\n",
    "b"
)


questions = [question1, question2, question3]


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for question in self.questions:
            print(question.prompt)
            userAnswer = input("Your answer (a/b/c/d): ").lower()

            if userAnswer == question.answer:
                print("Correct!\n")
                self.score += 1
            else:
                print("Wrong. The correct answer is:", question.answer)
                print()

        print("Quiz completed.")
        print("Your score is", self.score, "out of", len(self.questions))


quiz = Quiz(questions)
quiz.run()