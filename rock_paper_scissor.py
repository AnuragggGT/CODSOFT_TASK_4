# IMPORT ALL THE NECESSARY MODULES

import tkinter as tk
from tkinter import messagebox as msgbox
import random

#initialise the user_score and comp_score

user_score=0
comp_score=0 

#comment for the result display

tie_comms=["Honors even, and the drama lives on!","No winner, no loser—just pure competition!","All tied up—what a nail-biter!","Neither side blinked—it’s a perfect standoff!","A stalemate, but far from a dull affair!"]
win_comms=["Victory sealed—what a performance!","Clinched it in style—what a finish!","Triumph written all over","A commanding win and a statement made!"]
lose_comms=["Defeat today, lessons for tomorrow.","A tough loss, but the spirit was there.","The battle’s lost, but the war goes on.","Beaten, but not broken."]


#decide the winner of the game

def winner(user,comp):
    if user == comp:
        return "TIE"
    elif (user == "Rock" and comp == "Scissors") or (user == "Paper" and comp == "Rock") or(user == "Scissors" and comp == "Paper"):
        return "WIN"
    else:
        return "LOSE"


#start the game 

def play(user_choice):
    
    #set the global user_score,comp_score

    global user_score,comp_score

    #take the choice of the computer

    comp_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = winner(user_choice,comp_choice)

    if result == "WIN":
        user_score += 1
        comment = random.choice(win_comms)
        outcome = "You Win!"
    elif result == "LOSE":
        comp_score += 1
        comment = random.choice(lose_comms)
        outcome = "Computer Wins!"
    else:
        comment = random.choice(tie_comms)
        outcome = "It's a Tie!"


    #config the labels to display the desired outputs

    result_label.config(text=f"You: {user_choice}\nComputer: {comp_choice}\nResult: {outcome}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")
    comment_label.config(text=f"{comment}")

# Exit the game

def quit():
    msg = msgbox.askyesno("Quit", "Do you want to quit the game ?")
    if msg:
        root.destroy()
    
#setup the GUI 

root = tk.Tk()
root.title("ROCK PAPER SCISSORS GAME")
root.geometry("600x600")
root.config(bg="#E4A3A3")

title = tk.Label(root, text="ROCK PAPER SCISSORS GAME", font=("Helvetica", 20, "bold"), bg="#E4A3A3", fg="#333")
title.pack(pady=10)

comment_label = tk.Label(root, text="", font=("Helvetica", 15), bg="#E4A3A3")
comment_label.pack(pady=20)


result_label = tk.Label(root, text="", font=("Helvetica", 15), bg="#E4A3A3")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 15), bg="#E4A3A3")
score_label.pack(pady=20)

# Buttons
btn_frame = tk.Frame(root, bg="#E4A3A3")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", font=("Helvetica", 15), width=12, command=lambda: play("Rock"), bg="#FB5959")
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="Paper", font=("Helvetica", 15), width=12, command=lambda: play("Paper"), bg="#7BFA7B")
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="Scissors", font=("Helvetica", 15), width=12, command=lambda: play("Scissors"), bg="#8282FB")
scissors_btn.grid(row=0, column=2, padx=10)

quit_btn = tk.Button(root, text="Quit", font=("Helvetica", 15), command=quit, width=15, bg="#FF0000")
quit_btn.pack(pady=20)

root.mainloop()
