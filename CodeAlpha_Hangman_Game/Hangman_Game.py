import random

word_list = ["apple", "tiger", "chair", "robot", "plant"]
secret_word = random.choice(word_list)
display = ["_"] * len(secret_word)  

lives = 6

print("Welcome to Hangman Game!")
print("You have 6 incorrect guesses allowed.\n")

while lives > 0:
    
    print("Word: ", " ".join(display))
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print("You already guessed that letter.\n")
        continue
    
    if guess in secret_word:
        for position in range(len(secret_word)):
            if secret_word[position] == guess:
                display[position] = guess
        print("Correct guess!\n")
    else:
        lives -= 1
        print("Wrong guess!")
        print("Remaining lives:", lives, "\n")
    
    if "_" not in display:
        print("Congratulations! You won!")
        print("The word was:", secret_word)
        break

if lives == 0:
    print("You lost!")
    print("The correct word was:", secret_word)
