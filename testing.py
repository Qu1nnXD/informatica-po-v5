import random

# galgje 
print("Welkom bij galgje!")
woorden = ["welkom", "galgje", "leugen", "babbelen", "schrijver"]
woord = random.choice(woorden)
geradenWoord = ["_"] * len(woord)
print("Dit is je woord. " + "-" * len(woord))
run = True
pogingen = 0
gokken = list()
alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


while run:

  if "".join(geradenWoord) == woord:
    print("Je hebt het woord geraden!")
    break
  gok = input("Raad een letter: ")
  if gok in gokken:
    print("je hebt deze letter al geraden")
  if gok in alfabet:
    if gok in woord:
      gokken.append(gok)
    for aantalLetters in range(0, len(woord)):
      if gok == woord[aantalLetters]:
        geradenWoord[aantalLetters] = gok
        print(geradenWoord)
        gokken.append(gok)
    if gok not in woord:
      print("Helaas de letter " + gok + " zit niet in het woord.")
      pogingen = pogingen + 1
      print(geradenWoord)
      gokken.append(gok)
    if pogingen >= 6:
      print("Helaas je hebt het woord niet geraden. ")
      run = False
  else:
    print("Dit is geen geldige letter.")