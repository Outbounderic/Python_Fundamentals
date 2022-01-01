from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for i in question_data:
    mod_data = Question(i['text'], i['answer'])
    question_bank.append(mod_data)

new_q = QuizBrain(question_bank)
new_q.next_question()