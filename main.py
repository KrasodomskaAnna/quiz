import tkinter as tk
from tkinter import messagebox, ttk
from tkmacosx import Button
from ttkbootstrap import Style
from bsk_test_1.quiz_data import quiz_data


def submit_question():
    global choices, current_question
    question = quiz_data[current_question]

    # Count correct
    correct = 0
    max_correct = 0
    correct_answers = []
    incorect_answers = []
    for i in range(4):
        choice = question["choices"][i]
        if choice.keys().__contains__("correct"):
            max_correct += 1
            correct_answers.append(i)
            if choices.count(i) > 0:
                correct += 1
        elif choices.count(i) > 0:
            incorect_answers.append(i)

    # Display points
    global score
    if correct == max_correct and len(incorect_answers) == 0:
        score += 1
        score_label.config(text="Score: {}/{}".format(score, current_question))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        score += round(correct/max_correct, 2) if max_correct > 0 else 0
        score_label.config(text="Score: {}/{}".format(score, current_question))
        feedback_label.config(text="Incorrect!", foreground="red")
        for i in range(len(choice_btns)):
            button = choice_btns[i]
            if correct_answers.count(i) > 0:
                button.configure(bg=color_btn_correct)
            elif incorect_answers.count(i) > 0:
                button.configure(bg=color_btn_incorrect)


    next_button.config(state="normal")
    submit_button.config(state="disabled")
    choices.clear()

def show_question():
    question = quiz_data[current_question]
    qs_label.configure(text=question["question"])
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i]["answer"], state="normal")
    feedback_label.config(text="")
    next_button.config(state="disabled")
    submit_button.config(state="normal")

def check_answer(choice):
    global choices

    if choices.count(choice) == 0:
        choices.append(choice)
        choice_btns[choice].configure(bg=color_btn_is_selected)
    else:
        choices.remove(choice)
        choice_btns[choice].configure(bg=color_btn_not_selected)


def next_question():
    global current_question, choices
    current_question += 1
    if current_question < len(quiz_data):
        choices.clear()
        for i in range(4):
            choice_btns[i].configure(bg=color_btn_not_selected)
        info_label.config(text="Pozostało {} pytań".format(len(quiz_data) - current_question))
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()


# initialize
score = 0
current_question = 1
choices = []

# Window
root = tk.Tk()
root.title("Quiz App")
root.geometry("620x550")

# Style
style = Style(theme="flatly")
style.configure("TLabel", font=("Helvetica", 17))
style.configure("TButton", font=("Helvetica", 16))

# colors
color_btn_not_selected = '#2c3f50'
color_btn_is_selected = '#000'
color_btn_correct = '#75FFAE'
color_btn_incorrect = '#FA675D'

# Question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Choice buttons
choice_btns = []
for i in range(4):
    button = Button(
        root,
        bg=color_btn_not_selected,
        activebackground='#415060',
        foreground='white',
        justify='center',
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Submit button
submit_button = ttk.Button(
    root,
    text="Submit",
    command=submit_question
)
submit_button.pack(pady=10)

# Next button
next_button = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_button.pack(pady=10)

# Info label
info_label = ttk.Label(
    root,
    text="Pozostało {} pytań".format(len(quiz_data) - current_question),
    anchor="center",
    padding=10,
    justify='center',
    font=10,
    wraplength=600
)
info_label.pack(pady=10)

# Feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10,
    justify='center',
    wraplength=600
)
feedback_label.pack(pady=10)

# Show the first question
show_question()

root.mainloop()
