# CodeAlpha_PythonProgrammingTasks

This repository contains a collection of Python projects developed as part of the CodeAlpha internship program. Each project is a standalone console application demonstrating different programming concepts.

## Projects

### 1. ChatBot

A simple, rule-based chatbot that interacts with users on the command line.

#### Features
- Responds to predefined inputs like "hello", "how are you", and "bye".
- Provides a help message for available commands.
- Runs in a continuous loop until the user types "bye".

#### How to Run
1. Navigate to the `chatbot` directory.
   ```sh
   cd chatbot
   ```
2. Run the Python script.
   ```sh
   python chatbot.py
   ```
3. Interact with the chatbot in your terminal.

---

### 2. Email Extractor

A utility script to extract, sort, and categorize email addresses from a given text file.

#### Features
- Reads content from a user-specified file.
- Uses regular expressions to find all valid email addresses.
- Removes duplicate entries and sorts the list alphabetically.
- Filters and lists Gmail addresses separately.
- Saves the results to a user-specified output file.

#### How to Run
1. Navigate to the `email_extractor` directory.
   ```sh
   cd email_extractor
   ```
2. Run the script.
   ```sh
   python email_extractor.py
   ```
3. When prompted, enter the input file name (e.g., `dataset.txt`).
4. Enter a name for the output file (e.g., `emails.txt`). The results will be saved there.

---

### 3. Hangman Game

A classic command-line implementation of the Hangman word-guessing game.

#### Features
- Selects a random word from a predefined list.
- Displays the word with blanks for unguessed letters.
- Tracks correctly and incorrectly guessed letters.
- Limits the player to a maximum of 6 wrong guesses.
- Provides a main menu to start a new game or exit.

#### How to Run
1. Navigate to the `hangman` directory.
   ```sh
   cd hangman
   ```
2. Execute the script.
   ```sh
   python hangman.py
   ```
3. Follow the on-screen instructions to play the game.
