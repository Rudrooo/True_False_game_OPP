class Brain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def still_has_question(self):
        return self.question_number< len(self.question_list)


    def next_question(self):

        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_ans=input(f"Q.{self.question_number} : {current_question.text}?(true/false):")
        self.check_answer(user_ans,current_question.ans)

    def check_answer(self,u_ans,c_ans):
        if u_ans.lower()==c_ans.lower():
            self.score+=1
            print(f"You got it right!")
        else:
            print("That's wrong!")

        print(f"The correct answer was: {c_ans}")
        print(f"Yor current score is: {self.score}/{self.question_number}")
