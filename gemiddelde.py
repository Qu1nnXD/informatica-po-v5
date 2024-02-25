# intro gemiddelde berekenen voor max 4 cijfers
print("Welkom bij het berekenen van je voldoende! \n")
# cijfers en wegingen invoeren door middel van lijsten
cijfers = [float(input("Noem een cijfer: "))]
weging = [float(input("Noem de weging van dit cijfer: "))]
cijfers.append(float(input("Noem nog een cijfer: ")))
weging.append(float(input("Noem de weging van dit cijfer: ")))
cijfers.append(float(input("Noem nog een cijfer: ")))
weging.append(float(input("Noem de weging van dit cijfer: ")))
cijfers.append(float(input("Noem nog een cijfer: ")))
weging.append(float(input("Noem de weging van dit cijfer: ")))
# variabelen toewijzen 
aantalWegingen = len(weging)
aantalCijfers = len(cijfers)
totaalCijfers = 0
totaalWegingen = 0
gemiddeldeCijfers = []
# for loop om de wegingen van cijfers correct te gebruiken
for i in range(0, aantalCijfers):
    gemiddeldeCijfers.append(cijfers[i] * weging[i])
 
# gemiddelde berekenen en weergeven of dit voldoende is of niet door gebruik te maken van if/else-statements
if sum(gemiddeldeCijfers) / sum(weging) >= 5.5:
  print("Je staat een voldoende voor dit vak! :D")
else:
  print("Helaas sta je onvoldoende voor dit vak :( ")
input("Berekenen beëindigd: Druk op Enter om te sluiten...") 
