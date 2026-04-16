import random

words = ["python", "hangman", "computer", "programming", "developer"]

def hangman():
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    while wrong_guesses < max_wrong:
        
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord:", display_word.strip())
        
        if "_" not in display_word:
            print("🎉 You guessed the word correctly:", word)
            return   # cleaner than break
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input.")
            continue
        
        if guess in guessed_letters:
            print("⚠️ Already guessed.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("✅ Correct!")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! Attempts left: {max_wrong - wrong_guesses}")

    print("\n💀 You lost! The word was:", word)


# Main menu
playing = True

while playing:
    print("\n🎮 Welcome to Hangman!")
    print("1. Start Game")
    print("2. Exit")
    
    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        hangman()
    else:
        print("Goodbye!")
        playing = False

input("Press Enter to exit...")