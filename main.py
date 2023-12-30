from cgitb import text
from tkinter import *
import math

from sklearn.utils import column_or_1d
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_word.config(text="Timer", fg=GREEN)
    check_box.config(text="")
    global reps
    reps = 0
    # ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    # count_down(5*60)
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer_word.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN*60)
        timer_word.config(text="Work", fg=GREEN)

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer_word.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_box.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_word = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer_word.grid(column=1, row=0)
check_box = Label(font=(FONT_NAME, 14), bg=YELLOW, fg=GREEN)
check_box.grid(column=1, row=2)


# Button
start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)


window.mainloop()
