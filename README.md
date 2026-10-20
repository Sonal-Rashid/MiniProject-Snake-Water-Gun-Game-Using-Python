# Snake Water Gun Game
It is a beginner-friendly project that strengthens logic-building skills and introduces real-world programming flow in Python.

## 📊 Project Overview 
The goal of this mini project is to build a simple command-line game using Python where the user plays Snake–Water–Gun against the computer. This project helps reinforce basic Python concepts in a fun and practical way. Here we have given the option for playing multiple rounds. At the end the player can review the total score too

## 🎮 Game Rules
- Snake drinks Water → Snake wins
- Water disables Gun → Water wins
- Gun kills Snake → Gun wins
- Same choice by both → Draw

## ✨ Program Explanation
1. Computer's Turn: The random module randomly selects Snake (s), Water (w), or Gun (g) for the computer.
2. User's Turn: The player enters their choice (s, w, or g). The input is converted to lowercase to accept uppercase or lowercase letters.
3. Input Validation: The program checks whether the user's choice is valid. Invalid inputs are rejected without counting them as a round.
4. Game Logic: A custom function compares the player's and computer's choices and determines the outcome:
    - True — The player wins.
    - False — The player loses.
    - None — The round ends in a draw.
5. Multiple Rounds: A while loop allows the player to play multiple rounds until they choose to stop.
6. Score Tracking: Three counters keep track of the total wins, losses, and draws. The score is updated after each valid round.
7. Live Scoreboard: The current score is displayed after every round, allowing the player to track their performance.
8. Final Score: When the player exits the game, the program displays the final number of wins, losses, and draws.
9. Formatted Output: f-strings are used to display the player's choice, the computer's choice, and the scores in a readable format.

## 🛠️ Requirements
Python 3

## ▶️ How to Run
1. Clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:
   
   ```bash
   python3 main.py
   ```
   
## 📚 Concepts Practiced
- Python functions and return values
- Conditional statements
- While loops
- User input and input validation
- Random choices
- Score counters
