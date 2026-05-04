# Rock Paper Scissors — Smart AI Edition

A desktop game built with Python's `tkinter` library where you play Rock Paper Scissors against an AI that **learns your patterns** and adapts its strategy over time.

---

## Features

- **Smart AI** — tracks your move history and predicts your next choice, countering it with 70% probability
- **Live Scoreboard** — tracks User vs AI score throughout the session
- **Color-coded Results** — green for win, red for loss, blue for tie
- **Reset Game** — wipes scores and AI memory for a fresh start
- **Clean Dark UI** — modern dark-themed interface built with tkinter

---

## How the AI Works

The AI maintains a frequency count of your past moves (rock, paper, scissors). On each turn:

1. It finds the move you've played most often
2. With **70% probability**, it plays the counter to that move
3. With **30% probability**, it plays randomly (to stay unpredictable)

The more you play, the smarter it gets — try mixing up your moves to beat it!

---

## Requirements

- Python 3.x
- `tkinter` (included with standard Python installations)

No external packages needed.

---

## How to Run

```bash
python rps_game.py
```

---

## Project Structure

```
rps_game.py       # Main game file (all logic + UI in one file)
README.md         # This file
requirements.txt  # Dependency list
```

---

## Screenshots

| State     | Description                          |
|-----------|--------------------------------------|
| Start     | "Make your move!" prompt shown       |
| Win       | Result text turns green              |
| Lose      | Result text turns red                |
| Tie       | Result text turns blue               |

---

## Author
M.Bilal Qadir 

Built as a fun Python mini-project demonstrating adaptive AI with a tkinter GUI.
