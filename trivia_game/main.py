#----------------------
# Zach Ignacio
# Import and use libraries in this code
# Main Code
#----------------------

import random
from modules.questions import trivia_questions, welcome_message, get_random_question
from modules.game_logic import check_answer

def main():
    print(welcome_message)
    score = 0

    for _ in range(3):  # Ask 3 questions
        question, answer = get_random_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()

        if check_answer(user_answer, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The right answer was: {answer}")

    print(f"Game over! Your final score is {score}/3.")

if __name__ == "__main__":
    main()

# modules/questions.py
# This module contains trivia questions and helper functions.
import random

trivia_questions = {
    "What is the capital of France?": "paris",
    "What is 5 + 7?": "12",
    "What is the largest ocean on Earth?": "pacific"
}

welcome_message = "Welcome to the Trivia Game! Try to answer the questions correctly."

def get_random_question():
    question = random.choice(list(trivia_questions.keys()))
    return question, trivia_questions[question]

# modules/game_logic.py
# This module contains the function to check the correctness of answers.
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer
