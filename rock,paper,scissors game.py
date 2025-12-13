import tkinter as tk
import random

# -------------------- SMART AI MEMORY --------------------
user_history = {"rock": 0, "paper": 0, "scissors": 0}

def smart_ai():
    total = sum(user_history.values())
    if total == 0:
        return random.choice(choices)

    predicted = max(user_history, key=user_history.get)

    # 70% chance to counter, 30% random
    if random.random() < 0.7:
        if predicted == "rock":
            return "paper"
        elif predicted == "paper":
            return "scissors"
        else:
            return "rock"
    else:
        return random.choice(choices)

# -------------------- GAME LOGIC --------------------
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def highlight_winner(winner):
    if winner == "user":
        result_label.config(fg="green")
    elif winner == "AI":
        result_label.config(fg="red")
    else:
        result_label.config(fg="blue")  # tie

def play(user_choice):
    global user_score, computer_score

    user_history[user_choice] += 1
    computer_choice = smart_ai()

    # Decide winner
    if user_choice == computer_choice:
        result = f"Both chose {user_choice}. It's a Tie!"
        highlight_winner("tie")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = f"You chose {user_choice}, AI chose {computer_choice}. You Win!"
        user_score += 1
        highlight_winner("user")
    else:
        result = f"You chose {user_choice}, AI chose {computer_choice}. AI Wins!"
        computer_score += 1
        highlight_winner("AI")

    # Update UI text
    result_label.config(text=result)
    score_label.config(text=f"User: {user_score}     AI: {computer_score}")

# -------------------- RESET GAME --------------------
def reset_game():
    global user_score, computer_score, user_history
    user_score = 0
    computer_score = 0
    user_history = {"rock": 0, "paper": 0, "scissors": 0}
    score_label.config(text="User: 0     AI: 0")
    result_label.config(text="Make your move!", fg="white")

# -------------------- WINDOW --------------------
window = tk.Tk()
window.title("Rock Paper Scissors - Smart AI Edition")
window.geometry("480x400")
window.config(bg="#1e1e1e")

# -------------------- TITLE --------------------
title = tk.Label(window, text="Rock • Paper • Scissors", font=("Arial", 22, "bold"), bg="#1e1e1e", fg="white")
title.pack(pady=15)

# -------------------- SCOREBOARD --------------------
score_label = tk.Label(window, text="User: 0     AI: 0", font=("Arial", 16), bg="#1e1e1e", fg="white")
score_label.pack()

result_label = tk.Label(window, text="Make your move!", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="white")
result_label.pack(pady=15)

# -------------------- BUTTONS --------------------
btn_frame = tk.Frame(window, bg="#1e1e1e")
btn_frame.pack(pady=15)

btn_rock = tk.Button(btn_frame, text="Rock", width=12, height=2, font=("Arial", 14), command=lambda: play("rock"))
btn_rock.grid(row=0, column=0, padx=10)

btn_paper = tk.Button(btn_frame, text="Paper", width=12, height=2, font=("Arial", 14), command=lambda: play("paper"))
btn_paper.grid(row=0, column=1, padx=10)

btn_scissors = tk.Button(btn_frame, text="Scissors", width=12, height=2, font=("Arial", 14),
                         command=lambda: play("scissors"))
btn_scissors.grid(row=0, column=2, padx=10)

# Reset button
reset_btn = tk.Button(window, text="Reset Game", width=20, height=2, font=("Arial", 14),
                      command=reset_game, bg="#ff5555", fg="white")
reset_btn.pack(pady=10)

# -------------------- RUN --------------------
window.mainloop()
