questions = [
    {
        "question": "Wh0 has 70plus centuries in indian cricket team?",
        "options": ["A) rohit", "B) kohli", "C) kl rahul", "D) Ms dhoni"],
        "answer": "B"
    },
    {
        "question": "Wh0 directed the bahubali movie?",
        "options": ["A) Prashanth neel", "B) Puri jaganadh", "C) Ss Rajmouli", "D) Trivikram"],
        "answer": "C"
    },
    {
        "question": "What is the capital of andhra pradesh?",
        "options": ["A) Amaravati", "B) Visakhapatnam", "C) Anakapalle", "D) Srikakulam"],
        "answer": "A"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for carbon dioxide?",
        "options": ["A) H2O", "B) CO2", "C) O2", "D) H2O2"],
        "answer": "B"
    }
]
def run_quiz(questions):
    score = 0
    total_questions = len(questions)
    for idx, question in enumerate(questions, 1):
        print(f"Question {idx}: {question['question']}")
        for option in question['options']:
            print(option)
        answer = input("Your answer (A, B, C, D): ").strip().upper()
        if answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}\n")
    print(f"Your final score is {score} out of {total_questions}")

run_quiz(questions)
