import random
# dit werkt bijna
# galgje 
print("Welkom bij galgje!")
woorden = ["welkom", "galgje", "leugen", "babbelen", "schrijver"]
woord = random.choice(woorden)
geradenWoord = ["_"] * len(woord)
print("Dit is je woord. " + "-" * len(woord))
run = True


while run:
  gok = input("Raad een letter: ")
  if gok in woord:
    print("Goed geraden!")
  for aantalLetters in range(0, len(woord)):
    if gok == woord[aantalLetters]:
      geradenWoord[aantalLetters] = gok

    # als geradenWoord goed is, run is False

  print(geradenWoord)