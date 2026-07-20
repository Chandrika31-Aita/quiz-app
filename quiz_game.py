# Import random library to select random questions
import random

# Variable to store the user's score
score = 0

# Question bank containing all quiz questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "What is 10 + 20?",
        "options": ["A. 10", "B. 20", "C. 30", "D. 40"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "How many months are there in a year?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. function", "C. define", "D. def"],
        "answer": "D"
    },
    {
        "question": "What is 5 * 6?",
        "options": ["A. 30", "B. 25", "C. 35", "D. 40"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "How many hours are there in a day?",
        "options": ["A. 12", "B. 18", "C. 24", "D. 30"],
        "answer": "C"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Which data type stores text in Python?",
        "options": ["A. int", "B. float", "C. str", "D. bool"],
        "answer": "C"
    },
    {
        "question": "Which loop repeats until a condition becomes false?",
        "options": ["A. for", "B. while", "C. if", "D. else"],
        "answer": "B"
    },
    {
        "question": "What is 100 / 10?",
        "options": ["A. 5", "B. 20", "C. 10", "D. 15"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for equality comparison?",
        "options": ["A. =", "B. !=", "C. ==", "D. >"],
        "answer": "C"
    }
]

# Function to conduct the quiz
def play_quiz():
    global score

    # Randomly select 5 questions from the question bank
    selected_questions = random.sample(questions, 5)

    # Display questions one by one
    for q in selected_questions:
        print("\n" + q["question"])

        # Display all options
        for option in q["options"]:
            print(option)

        # Take answer from the user
        answer = input("Enter your answer (A/B/C/D): ").upper()

        # Check whether the answer is correct
        if answer == q["answer"]:
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")
            print("Correct Answer is:", q["answer"])

# Function to display the final result
def show_result():
    print("\n===== QUIZ RESULT =====")
    print("Your Score:", score)
    print("Total Questions: 5")

    # Display performance based on score
    if score == 5:
        print("Outstanding!")
    elif score >= 3:
        print("Good Job!")
    else:
        print("Keep Practicing!")

# Main menu loop
while True:
    print("\n===== PYTHON QUIZ GAME =====")
    print("1. Start Quiz")
    print("2. Exit")
    # Take menu choice from the user
    choice = input("Enter Choice: ")
    # Start the quiz
    if choice == "1":
        score = 0
        play_quiz()
        show_result()

    # Exit the program
    elif choice == "2":
        print("Thank You for Playing!")
        break

    # Handle invalid choices
    else:
        print("Invalid Choice! Please try again.")
