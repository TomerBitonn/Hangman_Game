# 🕹️ Hangman Game in Python

A classic **Hangman** game implemented in Python using clean code and modular design principles.

## 📁 Project Structure

```
Hangman_Game/
├── main.py # Main file to run the game
├── hangman_functions.py # All reusable game functions
├── constants.py # Constants used throughout the game
├── hangman_words.txt # Word bank for the game
├── README.md # Project documentation (this file)
```

## ▶️ How to Run

1. Make sure you have Python 3 installed on your system.
2. Clone the repository or download the project files.
3. Open a terminal in the project folder.
4. Run the game:

```bash
python main.py
```

## 🔧 Features
Word bank loaded from a text file (hangman_words.txt)

Separation of logic using hangman_functions.py

Constants such as number of tries and messages managed in constants.py

Clear structure and readable code

Validations for input and repeated guesses

ASCII art for visual feedback

## 📝 Notes
You can add more words to the hangman_words.txt file to increase difficulty.

The game ends when the user either guesses the word correctly or runs out of attempts.
