import random

# galgje 
print("Welkom bij galgje!")
woorden = ["welkom", "galgje", "leugen", "babbelen", "schrijver"]
woord = random.choice(woorden)
print("Dit is je woord. " + "-" * len(woord))
gok1 = input("Raad een letter: ")

if gok1 in woord:
  print("Goed geraden!")
 