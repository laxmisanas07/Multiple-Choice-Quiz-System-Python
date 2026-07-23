import sys

class QuizSystem:

    def __init__(self):
        self.questions = []
        self.student_name = ""
        self.student_id = ""

        self.score = 0
        self.correct = 0
        self.wrong = 0

    # Student Registration
    def register_student(self):
        self.student_name = input("Enter Student Name: ")
        self.student_id = input("Enter Student ID: ")
        print("\nStudent Registered Successfully!\n")

    # Admin Add Questions
    def add_questions(self):

        n = int(input("Enter Number of Questions: "))

        for i in range(n):
            print(f"\nQuestion {i+1}")

            question = input("Enter Question: ")

            options = []

            for j in range(4):
                option = input(f"Enter Option {j+1}: ")
                options.append(option)

            while True:
                answer = int(input("Enter Correct Option (1-4): "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Invalid choice! Enter between 1 and 4.")

            self.questions.append({
                "question": question,
                "options": options,
                "answer": answer
            })

        print("\nQuestions Added Successfully!\n")

    # Start Quiz
    def start_quiz(self):

        if self.student_name == "":
            print("\nPlease Register Student First!\n")
            return

        if len(self.questions) == 0:
            print("\nNo Questions Available!\n")
            return

        # Reset Score
        self.score = 0
        self.correct = 0
        self.wrong = 0

        print("\n===== QUIZ STARTED =====\n")

        for i, q in enumerate(self.questions):

            print(f"Question {i+1}: {q['question']}")

            for j in range(4):
                print(f"{j+1}. {q['options'][j]}")

            while True:
                try:
                    choice = int(input("Enter your choice (1-4): "))
                    if 1 <= choice <= 4:
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except:
                    print("Invalid Input!")

            if choice == q["answer"]:
                print("Correct!\n")
                self.score += 5
                self.correct += 1
            else:
                print("Wrong!")
                print("Correct Answer:",
                      q["options"][q["answer"]-1], "\n")
                self.wrong += 1

        print("Quiz Completed!\n")

    # Display Result
    def display_result(self):

        if self.student_name == "":
            print("No Student Registered.")
            return

        print("\n========== RESULT ==========")
        print("Student Name :", self.student_name)
        print("Student ID   :", self.student_id)
        print("Correct      :", self.correct)
        print("Wrong        :", self.wrong)
        print("Total Score  :", self.score)
        print("============================\n")


# Main Program

quiz = QuizSystem()

while True:

    print("========== QUIZ MENU ==========")
    print("1. Register Student")
    print("2. Add Questions (Admin)")
    print("3. Start Quiz")
    print("4. Display Result")
    print("5. Exit")

    try:
        choice = int(input("Enter Your Choice: "))
    except:
        print("Invalid Input!\n")
        continue

    if choice == 1:
        quiz.register_student()

    elif choice == 2:
        quiz.add_questions()

    elif choice == 3:
        quiz.start_quiz()

    elif choice == 4:
        quiz.display_result()

    elif choice == 5:
        print("Thank You!")
        sys.exit()

    else:
        print("Invalid Choice!\n")