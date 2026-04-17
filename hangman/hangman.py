import random
import os



# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



# Hangman Game
def hangman(words):
    if not words:
        print("No words available. Please add some words to the list.")
        return
    
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    clear_screen()

    while wrong_guesses < max_wrong:
        
        
        if guessed_letters:
            print("Guessed letters:", " ".join(guessed_letters))

        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord:", display_word.strip())
        
        if all(letter in guessed_letters for letter in word):
            print("🎉 You guessed the word correctly:", word)
            return   
        
        guess = input("Enter a letter: ").lower()
        clear_screen()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input.")
            continue
        
        if guess in guessed_letters:
            print("⚠️ Already guessed.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"✅ Correct! Wrong guesses: {wrong_guesses}/{max_wrong}")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! Attempts left: {max_wrong - wrong_guesses}")

    print("\n💀 You lost! The word was:", word)



# Main menu
def main(): 
    playing = True
    words = ["python", "hangman", "programming", "challenge", "developer", "algorithm", "function", "variable", "syntax", "debugging"]
    while playing:
        print("\n🎮 Welcome to Hangman!")
        print("1. Start Game")
        print("2. Exit")
        
        user_input = input("Enter your choice: ")
        
        if user_input == "1":
            hangman(words)
        elif user_input == "2":
            print("Goodbye!")
            playing = False
        else:
            print("Invalid choice... Please enter 1 or 2.")

    input("Press Enter to exit...")



# Run the main function
try:
    main()
except KeyboardInterrupt:
    print("\n\nProgram stopped by user... Goodbye!")