import random
from tkinter import *

# computer's choice
choices = ["rock", "paper", "scissor"]

# tkinter screen setup
window = Tk()
window.title("Rock-Paper-Scissor")
window.minsize(300, 300)
window.config(padx=20, pady=20)

# label
label = Label(text="ROCK PAPER SCISSOR")
label.config(padx=20, pady=20, font=("Arial", 24, "italic"), fg="Blue")
label.grid(row=0, column=0, columnspan=3)
label2 = ["Player", "VS", "Computer"]

col = 0
for i in label2:
    l = Label(text=i)
    l.config(pady=20, padx=20, font=("Arial", 24, "bold"))
    l.grid(row=1, column=col)
    col = col + 1

# entry window
entry = Entry(width=50)
entry.grid(row=2, column=0, columnspan=3)


def rock():
    r = "rock"
    entry.delete(0, END)
    entry.insert(0, r)


def paper():
    p = "paper"
    entry.delete(0, END)
    entry.insert(0, p)


def scissor():
    s = "scissor"
    entry.delete(0, END)
    entry.insert(0, s)


# button
cl = 0
for b in choices:
    if b == "rock":
        b1 = Button(text=b, pady=10, padx=10, command=rock)
        b1.grid(row=3, column=cl)
    elif b == "paper":
        b1 = Button(text=b, pady=10, padx=10, command=paper)
        b1.grid(row=3, column=cl)
    else:
        b1 = Button(text=b, pady=10, padx=10, command=scissor)
        b1.grid(row=3, column=cl)
    cl += 1


def play():
    c = entry.get()
    b = random.choice(choices)
    if b == c:
        z = f"Computer choose {b}.Game Tie"
        entry.delete(0, END)
        entry.insert(0, z)
    elif b == 'rock' and c == 'paper':
        z = f"Computer choose {b}.You Win!"
        entry.delete(0, END)
        entry.insert(0, z)
    elif b == 'rock' and c == 'scissor':
        z = f"Computer choose {b}.You Lose!"
        entry.delete(0, END)
        entry.insert(0, z)
    elif c == 'rock' and b == 'paper':
        z = f"Computer choose {b}.You Lose!"
        entry.delete(0, END)
        entry.insert(0, z)
    elif b == 'paper' and c == 'scissor':
        z = f"Computer choose {b}.You Win!"
        entry.delete(0, END)
        entry.insert(0, z)
    elif c == 'rock' and b == 'scissor':
        z = f"Computer choose {b}.You Win!"
        entry.delete(0, END)
        entry.insert(0, z)
    elif c == 'paper' and b == 'scissor':
        z = f"Computer choose {b}.You Lose!"
        entry.delete(0, END)
        entry.insert(0, z)


ply = Button(text="Play", command=play)
ply.grid(row=4, column=1, padx=20, pady=20)
window.mainloop()
