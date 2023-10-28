import random

word_list = ["apple", "baboon", "camel", "Tejaswi"]
Chosen_word = random.choice(word_list)


display = []
for letter in Chosen_word:
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(Chosen_word)):
        letter = Chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")