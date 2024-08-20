words= ["camel" , "love", "hate"]
import random

chosen= random.choice(words)
print(chosen)

guess= input("guess a letter").lower()
print(guess)

for letter in chosen:
    if letter==guess:
        print("right")
    else:
        print("wrong")