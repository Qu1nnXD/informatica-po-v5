### voorbeeld galgje
'''
import random

def choose_word():
    words = ["programmeren", "python", "galgje", "spel", "computer", "programma", "ontwikkelen"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def main():
    max_attempts = 6
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 0

    print("Welkom bij Galgje!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Raad een letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Voer a.u.b. één geldige letter in.")
            continue

        if guess in guessed_letters:
            print("Je hebt deze letter al geraden. Probeer een andere.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print("Helaas, de letter zit niet in het woord.")
            print(f"Je hebt nog {max_attempts - attempts} pogingen over.")

        print(display_word(word_to_guess, guessed_letters))

        if all(letter in guessed_letters for letter in word_to_guess):
            print("Gefeliciteerd! Je hebt het woord geraden.")
            break

        if attempts >= max_attempts:
            print("Helaas, je hebt al je pogingen gebruikt. Het woord was:", word_to_guess)
            break

if __name__ == "__main__":
    main()
'''
print("Fortnite")