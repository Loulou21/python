count = 0
listenote = []
while 1:
    notes = input("Veuillez saisir une note entre 0 et 20 : ")

    if notes == "fin":
        break
    else:
        notes=float(notes)
        if notes >= 0 and notes <= 20:
            
            listenote.append(notes)
            count = count + 1
        else:
            print("la valeur n'est pas entre 0 et 20")

print(listenote)
toto = listenote.sort() 
notemin = listenote[0]
notemax = listenote[count-1]

print("La note min : ",notemin)
print("La note max :",notemax)

count2 = 0
somme = 0
for i in range(len(listenote)):
    somme = somme + listenote[i]
    #count2 = count2 + 1
print(somme/count)