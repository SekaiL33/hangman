"""
<When all strokes drawn>
print("-" * 12)
for i in range(3):
    print("|" + " " * 10 +"|")

print("|" + " " * 10 + "O")
print("|" + " " * 10 + "|/")
print("|" + " " * 10 + "|\\")
print("|" + " " * 10 + "|")
print("|" + " " * 10 + "/\\")
"""

"""Simple Hangman Game"""

import os

def print_hangman(display_lines):
    
    for line in range(7):
        if line == 1:
            for j in range(3):
                print(display_lines[line])
        else:
            print(display_lines[line])

def add_stroke(strokes, mistake, display_lines):
    
    for line in strokes[mistake][0]:
        display_lines[line] += strokes[mistake][1]

    return display_lines

def player_display(mistake, score, display_lines, guess_word, guess_char):
    print("\n----------<Player's turn>----------\n")
    print(f"   <Mistake : {mistake}>     <Score : {score}>\n")
    print_hangman(display_lines)
    print("\nWord: " + " ".join(guess_word))

    if guess_char != []:
        print("\nGuessed alphabets: ")
        if len(guess_char) <= 7:
            print(guess_char[0:len(guess_char)])
            print("\n"*2)

        elif len(guess_char) in range(8,15):
            print(guess_char[0:7])
            print(guess_char[7:len(guess_char)])
            print("\n"*1)

        elif len(guess_char) in range(15,22):
            print(guess_char[0:7])
            print(guess_char[7:14])
            print(guess_char[14:len(guess_char)])
            print()

        else:
            print(guess_char[0:7])
            print(guess_char[7:14])
            print(guess_char[14:21])
            print(guess_char[21:len(guess_char)])
            
    else:
        print("\n"*5)
    
    print("\n" + "-" * 37 + "\n")

# Print display for each stages of hangman
def print_stages(strokes, display_lines):
    print("Initial:")
    print_hangman(display_lines)

    for mistake in range(1,len(strokes) + 1):

        display_lines = add_stroke(strokes, mistake, display_lines)

        print(f"For mistake {mistake}:")
        print_hangman(display_lines)

# Stroke to add for each mistake count
strokes = {
        1 : ([2], "O"),
        2 : ([3, 4, 5], "|"),
        3 : ([3], "/"),
        4 : ([4], "\\"),
        5 : ([6], "/"),
        6 : ([6], "\\")
}

# Allowed characters a-z
allowed_char = []
for i in range(65,91):
    allowed_char.append(chr(i))

print("---------------Welcome to HangMan!----------------")
print("\t" * 6 + " |")
print("How to Play:" + "\t" * 5 + " |")
print("(A) 2 Players needed" + "\t" * 4 + " |")
print("\t" * 6 + " |")
print("(B) Riddler enters 1 word for Player to guess" + "\t" * 1 + " |")
print("\t" * 6 + " |")
print("(C) Player guess 1 character at a time:" + "\t" * 2 + " |")
print("    Each correct guess gets 1 point" + "\t" * 2 + " |")
print("    Each wrong guess adds a stroke to hangman" + "\t" * 1 + " |")
print("\t" * 6 + " |")
print("(D) Player wins if pinpoints the word before" + "\t" * 1 + " |")
print("    hangman drawing is completed, in 6 strokes" + "\t" * 1 + " |")
print("\t" * 6 + " |")
print("(E) Riddler wins otherwise" + "\t" * 3 + " |")
print("\t" * 6 + " |")

print(" \t<Enter to play> \t <q to quit>" + "\t" * 1 + " |")
print("\t" * 6 + " |")
print("-" * 50)

choice = input("Choice: ")

while choice.lower() != 'q':
   
    while True:
        os.system("cls")

        print("\n------------------<Riddler's turn>------------------\n")
        print("> Please enter ONE word.\n> Only character 'a' to 'z' allowed\n")

        word = input("Word: ")

        valid_count = 0
        for char in word:
            if char.upper() not in allowed_char:
                print("\nPlease enter ONE word with alphabets 'a' to 'z' only!")
                input("<Enter to continue>")
                break
            valid_count += 1

        if len(word) == 0:
            print("\nPlease enter ONE word!")
            input("<Enter to continue>")
            continue
        
        if valid_count == len(word):
            word = word.upper()
            break

    # initialize hangman display
    display_lines = [
        "-" * 12,
        "|" + " " * 10 +"|",
        "|" + " " * 10,
        "|" + " " * 10,
        "|" + " " * 10,
        "|" + " " * 10,
        "|" + " " * 10
    ]
    
    # initialize guess word display with "_"
    guess_word = list("_" * len(word)) # USING list() convert string into list of char
    guess_char = []

    # initialize mistake, score and combo counter
    mistake = 0
    score = 0 # Each correct guess gives 1 point

    while (mistake < len(strokes)) and ("_" in guess_word):
        os.system("cls")
        
        while True:
            player_display(mistake, score, display_lines, guess_word, guess_char)

            print("> Please guess ONE character only.\n> Only character 'a' to 'z' allowed")
            
            guess = input("\nGuess: ")

            if len(guess) != 1:
                print("\nPlease enter ONE character only!")
                input("<Enter to continue>")
                os.system("cls")
                continue
            else:
                if guess.upper() not in allowed_char:
                    print("\nPlease enter character 'a' to 'z' only!")
                    input("<Enter to continue>")
                    os.system("cls")
                    continue
            break

        if guess.upper() in guess_char:
            print(f"\nYou had guessed {guess.upper()}!\nTry another alphabet.")
            input("<Enter to continue>")
            continue
        else:
            guess_char.append(guess.upper())
        
        current_score = score
        for index in range(len(word)):
            if guess.upper() == word[index]:
                guess_word[index] = guess.upper()
                score += 1

        if score > current_score:
            print(f"\nGood guess! {guess} is in the word!")
            input("<Enter to continue>")
        else:
            mistake += 1
            display_lines = add_stroke(strokes, mistake, display_lines)
            
            print(f"\nBad luck... {guess} is not in the word...")
            input("<Enter to continue>\n")          

    os.system("cls")

    player_display(mistake, score, display_lines, guess_word, guess_char)
    
    if (mistake < len(strokes)) and ("_" not in guess_word):
        print(f"Congratulations! Player won!\nScore: {score}\n")
    else:
        print(f"Player lost... Better luck next time...\nScore: {score}\n")

    # Continue or quit
    print("<Enter to continue>\n<q to quit>")
    choice = input("Choice: ")

