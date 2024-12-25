import tkinter as tk
import random

def move_button():
    new_x = random.randint(0, 200)
    new_y = random.randint(0, 200)
    button.place(x=new_x, y=new_y)

def increase_score():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    move_button()

root = tk.Tk()
root.title("Click the Button Game")
root.geometry("300x300")

score = 0
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 14))
score_label.pack()

button = tk.Button(root, text="Click Me!", command=increase_score)
button.place(x=100, y=100)

root.mainloop()
