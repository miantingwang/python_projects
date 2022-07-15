from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    item = Question(q['question'], q['correct_answer'])
    question_bank.append(item)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.q_num}.")
