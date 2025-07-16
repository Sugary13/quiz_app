import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quizz_brain: QuizBrain):
        self.quiz = quizz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white",
                             highlightthickness=0,)
        self.question = self.canvas.create_text(150, 125, text="Question",
                                                fill='black',
                                                width=280,
                                                font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=25)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")

        self.true_button = tkinter.Button(image=self.true_img, highlightthickness=0, borderwidth=0,
                                          command=self.true_answer)
        self.true_button.grid(column=0, row=2)
        self.false_button = tkinter.Button(image=self.false_img, highlightthickness=0, borderwidth=0,
                                           command=self.false_answer)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, self.get_next_question)
