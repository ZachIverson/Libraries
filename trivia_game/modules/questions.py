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
