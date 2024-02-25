# Wordle door Rick Wolters, V5a
# Wordle intro
# Print een welkomstbericht en uitleg over het spel.

print("Welkom bij Wordle!")
print("Het doel van het spel is om het woord te raden.")
print("Je hebt hier 6 beurten voor")
print("Het woord bestaat uit 6 letters, dus vul ook een 6 letter lang woord in.")
print("Veel plezier!")

# Woordenlijst
# Een lijst met woorden waaruit het te woord wordt gekozen.

woordenlijst = ["letter", "oranje", "jammer", "hockey", "zwarte", "voeten", "galgje", "school", "klaver", "wordle", "schaap", "aapjes", "status", "cervix", "kindje", "school", "python", "zwaluw", "metaal", "methyl", "banaan", "schild", "ethaan", "aziaat", "europa", "afrika", "keizer", "koning", "idioot", "welkom", "sirene", "juiste", "racist", "borden", "twaalf"]

# Woord kiezen
# Kiest een willekeurig woord uit de woordenlijst.

import random
woord = random.choice(woordenlijst)

# zet de variabele goed als False.

goed = False

# Woord raden
# Loop 6 keer voor elke beurt.

for i in range(6):
    print(" ")
    # Vraagt om een gok.
    gok = input("Raad het woord: ")
    print(" ")
    # Controleert of de gok de juiste lengte heeft.
    if len(gok) != 6:
        print("Je moet een woord van 6 letters invoeren.")
        break
    # Als de gok hetzelfde is aan het woord zet 'goed' op True, en laat het spel eindigen.
    if gok == woord:
        print("Gefeliciteerd, je hebt het woord geraden!")
        goed = True
        break
    # Loop door elke letter in de gok.
    for j in range(6):
        # Als de letter op dezelfde plek in de gok en het woord zit.
        if gok[j] == woord[j]:
            print(gok[j], "is in het woord en op de juiste plek")
        # Als de letter wel in het woord zit maar niet op de juiste plek.
        elif gok[j] in woord:
            print(gok[j], "is in het woord maar niet op de juiste plek")
        # Als de letter niet in het woord zit.
        else:
            print(gok[j], "is niet in het woord")

# Als het woord niet geraden is na 6 beurten.
if not goed:
    print(" ")
    print("Volgende keer beter!")
