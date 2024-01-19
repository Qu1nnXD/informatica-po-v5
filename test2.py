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
# hangman
def hangman():
    global attempts

    print("Welkom bij Galgje!")
    print(displayed_word(word, guessed_letters))
    
    while True:
        guess = input("Guess a letter: ")
        if guess in guessed_letters:
            print("Die letter heb je al geraden! Probeer opnieuw!")
            continue
        guessed_letters.append(guess)
        if guess == word:
            print("Goed zo! Wat een topper! Je hebt het woord geraden")
            break
        if guess not in word:
            attempts -= 1
            print(f"Foute gok! Je hebt nog maar {attempts} pogingen!")
        print(displayed_word(word, guessed_letters))
        if "_" not in displayed_word(word, guessed_letters):
            print("Goed zo! Wat een topper! Je hebt het woord geraden")
            break
        if attempts == 0:
            print("Je hebt geen pogingen meer, sorry!")
            break
hangman()         