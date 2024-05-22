questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Berlin", "B) Madrid", "C) New Delhi", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Which is th largest Ocean in the World?",
        "options": ["A) The Pacific Ocean", "B) The Arctic Ocean", "C) The Atlantic Ocean", "D) The Indian Ocean"],
        "answer": "A"
    }
]
def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {q['answer']}\n")
    return score
def get_user_answer():
    valid_answers = ['A', 'B', 'C', 'D']
    while True:
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        if answer in valid_answers:
            return answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")
def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = get_user_answer()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {q['answer']}\n")
    return score
def display_final_score(score, total_questions):
    print(f"Your final score is {score} out of {total_questions}.")

def main():
    total_questions = len(questions)
    score = run_quiz(questions)
    display_final_score(score, total_questions)

if __name__ == "__main__":
    main()
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def get_user_answer(self):
        valid_answers = ['A', 'B', 'C', 'D']
        while True:
            answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
            if answer in valid_answers:
                return answer
            else:
                print("Invalid input. Please enter A, B, C, or D.")

    def run_quiz(self):
        for q in self.questions:
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = self.get_user_answer()
            if answer == q["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer is {q['answer']}\n")
        self.display_final_score()

    def display_final_score(self):
        print(f"Your final score is {self.score} out of {len(self.questions)}.")

def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "Which is th largest Ocean in the World?'?",
            "options": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Jane Austen"],
            "answer": "A"
        }
    ]
    
    quiz = Quiz(questions)
    quiz.run_quiz()

if __name__ == "__main__":
    main()
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def get_user_answer(self):
        valid_answers = ['A', 'B', 'C', 'D']
        while True:
            answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
            if answer in valid_answers:
                return answer
            else:
                print("Invalid input. Please enter A, B, C, or D.")

    def run_quiz(self):
        for q in self.questions:
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = self.get_user_answer()
            if answer == q["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer is {q['answer']}\n")
        self.display_final_score()

    def display_final_score(self):
        print(f"Your final score is {self.score} out of {len(self.questions)}.")

def main():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A) Berlin", "B) Madrid", "C) New Delhi", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A) The Pacific Ocean", "B) The Arctic Ocean", "C) The Atlantic Ocean", "D) The Indian Ocean"],
            "answer": "A"
        }
    ]
    
    quiz = Quiz(questions)
    quiz.run_quiz()

if __name__ == "__main__":
    main()
