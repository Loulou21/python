#Exo4.3
import random

couleurs = ["Pique","Trefle","Carreau","Coeur"]
valeurs =  [2,3,4,5,6,7,8,9,10,"valet","dame","roi","as"]
cartes = []
joueur1 = []
joueur2 = []
joueur3 = []
joueur4 = []

for i in couleurs:
  for j in valeurs:
    cartes.append([i,j])

random.shuffle(cartes)
count = 0
mod = 0
while len(cartes) != 0:
    for car in cartes:
      if mod == 0:
        joueur1.append(car)
        cartes.remove(car)
        count = count + 1
        mod = count % 4
      elif mod == 1:
        joueur2.append(car)
        cartes.remove(car)
        count = count + 1
        mod = count % 4
      elif mod == 2:
        joueur3.append(car)
        cartes.remove(car)
        count = count + 1
        mod = count % 4
      elif mod == 3:
        joueur4.append(car)
        cartes.remove(car)
        count = count + 1
        mod = count % 4

print(joueur1)
print(joueur2)
print(joueur3)
print(joueur4)
