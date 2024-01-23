# Wordle intro

print("Welkom bij Wordle!")
print("Het doel van het spel is om het woord te raden.")
print("Je hebt hier 6 beurten voor")
print("Het woord bestaat uit 6 letters, dus vul ook een 6 letter lang woord in.")
print("Veel plezier!")

# woordenlijst

woordenlijst = ["letter", "oranje", "jammer" , "appel" , "hockey" , "voeten" , "galgje" , "school" , "klaver" , "wordle" , "schaap" , "aapjes" , "status" , "cervix" , "piemel" , "school" , "python" , "zwaluw" , "metaal" , "methyl" , "banaan" , "schild" , "ethaan" , "aziaat" , "europa" , "afrika" , "keizer" , "koning" , "gister" , "welkom" , "sirene" , "juiste" , "zwarte" , "racist" , "borden" , "twaalf"]

# Woord kiezen

import random
woord = random.choice(woordenlijst)

# Woord raden

goed = False

for i in range(6):
    print(" ")
    gok = input("Raad het woord: ")
    print(" ")
    if gok == woord:
        print("Gefeliciteerd, je hebt het woord geraden!")
        goed = True
        break
    if len(gok) != 6:
        print("Je moet een woord van 6 letters invoeren.")
        break
    for j in range(6):
        if gok[j] == woord[j]:
                print(gok[j], "is in het woord en op de juiste plek")
        elif gok[j] in woord:
                print(gok[j], "is in het woord maar niet op de juiste plek")
        else:
                print(gok[j], "is niet in het woord")
        if len(gok) != 6:
                print("Je moet een woord van 6 letters invoeren.")
                print(" ")
                break          

if not goed:
  print(" ")
  print("Volgende keer beter!")