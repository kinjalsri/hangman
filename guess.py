import random
from hangwords import words
from hangmanlives import logo, stages

print(logo)

chosen = random.choice(words)


placeholder = "_ " * len(chosen)
print(placeholder)

game_over = False 
correctletters = []
lives = 6

while not game_over:

    print(f"you have {lives} lives left")
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen:
        if letter == guess or letter in correctletters:
            display += letter
            correctletters.append(letter)
        else:
            display += "_"
    
    print(display)

    if guess not in chosen:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            game_over = True
            print(f"The word was {chosen}\n")
                  
            print("     ***You lose***    ")

    if "_" not in display:
        game_over = True
        print("     ***You win***     ")
