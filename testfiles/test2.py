import random
guessed_letters = []
attempts = 6
max:attempts = 6
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ë', 'ä', 'ö', 'ü', 'ï', 'é', 'è']
# woord kiezen door middel van een lijst
def choose_word():
    words =["kaas", "ham", "boterham", "leverworst", "tosti", "frikandelbroodje", "saucijzenbroodje", "croissant", "hagelslag", "boter", "pindakaas", "chocopasta", "bolus", "zeehond", "melk", "chocolademelk", "fristi", "koffie", "thee", "papier", "computer", "telefoon", "financiën", "yuzu", "telecomprovider", "verantwoordelijkheid", "sympathie", "activiteit", "catastrofe", "anaal", "prostaatkanker", "maatschappij", "wappie", "vaccinatie", "liquidatie", "klimaatverandering", "koolstofdioxide", "uitdaging", "mensheid", "narcostaat", "douanepolitie", "zelfgenoegzaamheid", "meervoudigepersoonlijkheidsstoornis"]
    return random.choice(words)
word = choose_word()

# woorden/symbolen tonen met een for loop en if/else-statements
def displayed_word(word, guessed_letters):
    display = " "
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
# galgje beeldtoestanden
def draw_hangman():
    stages = [  # eindtoestand: hoofd, torso, beide armen, en beide benen
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # hoofd, torso, beide armen, en één been
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # hoofd, torso, en beide armen
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # hoofd, torso, één arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # hoofd en torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # hoofd
                """
                   --------
                   |      |
                   |      O
                   |      
                   |      
                   |     
                   -
                """,
                # begintoestand
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

# galgje functie definiëren en input-regels
def hangman(visual_mode = True):
    global attempts

    print("Welkom bij Galgje!")
    print(displayed_word(word, guessed_letters))
    
    while True:
        guess = input("Raad een letter of woord: ")
        if guess in guessed_letters:
            print(f"Die letter heb je al geraden! Probeer opnieuw! Je hebt nog {attempts} pogingen over.")
            continue
        else: 
            guessed_letters.append(guess)
            if guess == word:
                print("Supertof! Je hebt het woord in één keer geraden!")
                break
            if guess not in word:
                attempts -= 1
                print(f"Foute gok! Je hebt nog maar {attempts} pogingen!")
            print(displayed_word(word, guessed_letters))
            if "_" not in displayed_word(word, guessed_letters):
                print(f"Goed zo! Je hebt het woord geraden! Je had nog {attempts} pogingen over.")
                break
            if visual_mode:
                print(draw_hangman())
            if attempts == 0:
                print(f"Je hebt geen pogingen meer, sorry! Het woord was {word}.")
                break
            if guess not in letters:
                print(f"Speciale tekens, cijfers of geen invoer zijn/is niet toegestaan; probeer opnieuw. Je hebt nog {attempts} pogingen over.")
                attempts += 1
visual_mode = input("Wil je met beeld spelen? (ja/nee): ")
if visual_mode.lower() == "ja":
    hangman()
else:
    hangman(False)
input("Spel beëindigd: Druk op Enter om te sluiten...")
