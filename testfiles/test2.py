import random
guessed_letters = []
attempts = 6

# word choosing
def choose_word():
    words =["Kaas", "Ham", "Boterham", "Leverworst", "Tosti", "Frikandelbroodje"]
    return random.choice(words)
word = choose_word()

# displaying words
def displayed_word(word, guessed_letters):
    display = " "
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
# hangman visual stages
def draw_hangman():
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |      
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |      
                   |      
                   |     
                   -
                """
    ]
    return stages[attempts]

# hangman
def hangman(visual_mode = True):
    global attempts

    print("Welkom bij Galgje!")
    print(displayed_word(word, guessed_letters))
    
    while True:
        guess = input("Raad een letter: ")
        if guess in guessed_letters:
            print("Die letter heb je al geraden! Probeer opnieuw!")
            continue
        guessed_letters.append(guess)
        if guess == word:
            print("Supertof! Je hebt het woord in één keer geraden!")
            break
        if guess not in word:
            attempts -= 1
            print(f"Foute gok! Je hebt nog maar {attempts} pogingen!")
        print(displayed_word(word, guessed_letters))
        if "_" not in displayed_word(word, guessed_letters):
            print("Goed zo! Je hebt het woord geraden!")
            break
        if visual_mode:
            print(draw_hangman())
        if attempts == 0:
            print(f"Je hebt geen pogingen meer, sorry! Het woord was {word}.")
            break
visual_mode = input("Wil je met beeld spelen? (ja/nee): ")
if visual_mode.lower() == "ja":
    hangman()
else:
    hangman(False)   