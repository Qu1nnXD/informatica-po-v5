print("Welkom bij het berekenen van je voldoende! \n")
 
cijfers = [float(input("noem een cijfer goezoe: "))]
weging = [float(input("noem de weging van dit cijfer goezoe: "))]
cijfers.append(float(input("noem nog een cijfer goezoe: ")))
weging.append(float(input("noem de weging van dit cijfer goezoe: ")))
cijfers.append(float(input("noem nog een cijfer goezoe: ")))
weging.append(float(input("noem de weging van dit cijfer goezoe: ")))
cijfers.append(float(input("noem nog een cijfer goezoe: ")))
weging.append(float(input("noem de weging van dit cijfer goezoe: ")))
 
aantalWegingen = len(weging)
aantalCijfers = len(cijfers)
totaalCijfers = 0
totaalWegingen = 0
gemiddeldeCijfers = []
for i in range(0, aantalCijfers):
    gemiddeldeCijfers.append(cijfers[i] * weging[i])
 
 
if sum(gemiddeldeCijfers) / sum(weging) >= 5.5:
  print("voldonede goezoe")
else:
  print("L")