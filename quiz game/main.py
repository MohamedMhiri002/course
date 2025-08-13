from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for quest in question_data:
    question_text = quest["text"]
    question_answer = quest["answer"]
    question_bank.append(Question(question_text,question_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()