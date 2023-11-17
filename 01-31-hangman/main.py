import random

words = ['pencil', 'apple', 'window', 'repository', 'coding', 'hunger', 'copybook']
lives = 3

target = random.choice(words)
print(target)

coded_word = ["*" for i in target]

while lives != 0:  # Can be enhanced by getting 2 letters instead of 1
    if str(coded_word) == target:
        print(f"Yes, {target} is correct!")
        break
    else:
        letter = input("Guess the letter in the word: ").lower()
        if letter in target:
            coded_word[target.index(letter)] = letter
            print(str(coded_word))
        else:
            lives -= 1
            print(f"You haves {lives} left :(")


