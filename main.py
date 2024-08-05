import random as r
from hangman_logo import logo ,stages
#step1
from hangman_word import word_list
chosen_word = r.choice(word_list)
#step2
#  we can create a blank list in hangman
display = []

for letter in chosen_word:
    display.append("_")

#step3

end_of_game = False

lives = len(stages) - 1
print(logo)

while not end_of_game:
    word= input("Guess a letter:").lower()
    flag = 0
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == word:
            display[letter] =  word
            flag += 1
    print(f"{" ".join(display)}")
        
    if flag == 0:
        if lives<=1 :
            end_of_game =True
            print("game over!")
            print(f"correct word is a {chosen_word}")
        lives -= 1
    print(stages[lives])

    if  '_'  not in display:
        end_of_game =True
        print("you a Win!")
