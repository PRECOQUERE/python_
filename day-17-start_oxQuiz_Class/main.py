from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os
clear = lambda:os.system('cls')

#문제은행 만들기
question_bank = []
for question in question_data :
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

#퀴즈쇼 진행
clear()
while quiz.still_has_question():
    quiz.next_question()
   
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
