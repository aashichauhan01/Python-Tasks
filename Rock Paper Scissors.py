import random
from tkinter import *
from tkinter import messagebox

def start_game():
    game_frame.pack(pady=20)
    start_frame.pack_forget()
    result_label.config(text="")

def play(choice):
    uchoice = choice
    cchoice = random.choice(l)
    result_label.config(text=f"Your Choice: {uchoice} \nComputer's Choice: {cchoice}")
    
    global ucount, ccount
    if uchoice == cchoice:
        result_label.config(text=f"Draw!\n\nYour Choice: {uchoice}\nComputer's Choice: {cchoice}", fg="orange")
        ucount += 1
        ccount += 1
    elif (uchoice == "rock" and cchoice == "scissor") or (uchoice == "scissor" and cchoice == "paper") or (uchoice == "paper" and cchoice == "rock"):
        result_label.config(text=f"You win this round!\n\nYour Choice: {uchoice}\nComputer's Choice: {cchoice}", fg="green")
        ucount += 1
    else:
        result_label.config(text=f"Computer wins this round!\n\nYour Choice: {uchoice}\nComputer's Choice: {cchoice}", fg="red")
        ccount += 1
    
    rounds_played.set(rounds_played.get() + 1)
    
    if rounds_played.get() == 5:
        end_game()

def end_game():
    if ucount > ccount:
        messagebox.showinfo("Game Over", f"You win the game!\n\nYou: {ucount} \nComputer: {ccount}")
    elif ucount < ccount:
        messagebox.showinfo("Game Over", f"Computer wins the game!\n\nYou: {ucount} \nComputer: {ccount}")
    else:
        messagebox.showinfo("Game Over", f"It's a draw!\n\nYou: {ucount} \nComputer: {ccount}")
    reset_game()

def reset_game():
    global ucount, ccount
    ucount = 0
    ccount = 0
    rounds_played.set(0)
    start_frame.pack(pady=20)
    game_frame.pack_forget()
    result_label.config(text="")


window = Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")
window.config(bg="#dcdcdc")

l = ["rock", "scissor", "paper"]
ucount = 0
ccount = 0
rounds_played = IntVar(value=0)


start_frame = Frame(window, bg="#dcdcdc")
start_frame.pack(pady=20)

start_label = Label(start_frame, text="Rock Paper Scissors", font=('arial', 20, 'bold'), bg="#dcdcdc")
start_label.pack(pady=20)

start_button = Button(start_frame, text="Start Game", font=('arial', 14), bg="#4CAF50", fg="white", command=start_game)
start_button.pack(pady=10)

exit_button = Button(start_frame, text="Exit", font=('arial', 14), bg="#f44336", fg="white", command=window.quit)
exit_button.pack(pady=10)


game_frame = Frame(window, bg="#dcdcdc")

rock_button = Button(game_frame, text="Rock", font=('arial', 14), width=10, height=2, bg="#FFC107", command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

scissor_button = Button(game_frame, text="Scissor", font=('arial', 14), width=10, height=2, bg="#03A9F4", command=lambda: play("scissor"))
scissor_button.grid(row=0, column=1, padx=10, pady=10)

paper_button = Button(game_frame, text="Paper", font=('arial', 14), width=10, height=2, bg="#8BC34A", command=lambda: play("paper"))
paper_button.grid(row=0, column=2, padx=10, pady=10)

result_label = Label(game_frame, text="", font=('arial', 14), bg="#dcdcdc")
result_label.grid(row=1, column=0, columnspan=3, pady=20)

window.mainloop()

