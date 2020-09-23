#Eval Louis ADAM
#1 Bases
            #1.1

a = "toto"
b = "tata"
c = ""
c = b
b = a
a = c
print("la valeur de a est : ",a)
print("la valeur de b est : ",b)

            #1.2
            
val1 = int(input("Veuillez saisir une valeur : "))
res1 = val1 **2
print(res1)

            #1.3

val2 = int(input("Veuillez saisir un nombre : "))
if val2 < 0:
    print("le nombre est négatif")
elif val2 > 0:
        print("le nombre est positif")

            #1.4

val3 = int(input("Saisir une valeur 1 : "))
val4 = int(input("Saisir une valeur 2 : "))
somme1 = val3 * val4
if somme1 < 0:
    print("le produit est négatif")
elif somme1 > 0:
    print("le produit est positif")

            #1.5

val5 = int(input("Saisir la valeur de départ : "))
val6 = val5 + 10
for i in range(val5+1,val6+1):
    print(i)

            #1.6

val7 = int(input("Veuillez saisir un nombre : "))
somme2=0
for j in range(1,val7+1):
    somme2 = somme2 + j
print(somme2)

# Exercices d'approfondissement
            #2.1

jours = [31,28,31,30,31,30,31,31,30,31,30,31]
mois = ["January", "February", "March", "April", "May", "June", "July", "August ", "September", "October",
"November", "December"]
jours_semaine = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", " Saturday", "Sunday"]
count1 = 0
mj=[]
annee = []
dico_annee = {}
for k in jours:
    mj.append((k,mois[count1]))
    count1 = count1 +1
print(mj)

            #2.2
count2 = 0
for l in mois:
    for m in range(1, (mj[count2][0]+1)):
        test = (m,l)
        annee.append(test)
        
    count2 = count2 + 1
print(annee)
count3 = 0
test=0
for n in annee:
     for o in range(len(jours_semaine)):
     # dico_annee.update({n : jours_semaine[count2]})
        count3 = count3 +1
     dico_annee[n] = jours_semaine[o]

print(dico_annee)


for p in dico_annee:
    if p == (28, 'October'):
        print("Le 28 octobre correspond à un ",dico_annee[p])
