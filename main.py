from question_model import Question
from data import question_data
from quiz_brain import Brain
question_bank=[]
for question in question_data:
    q_text=question["text"]
    q_ans=question["answer"]
    new_ques=Question(q_text,q_ans)
    question_bank.append(new_ques)

print(question_bank)



quiz=Brain(question_bank)

while quiz.still_has_question():

    quiz.next_question()

print("You completed the quiz.")
print(f"Your Final score is {quiz.score}/{quiz.question_number}")