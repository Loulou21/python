prenom = ""
nom = ""
liste = []
while 1:
    prenom = input("Saisir le prénom : ")
    if prenom == "FIN":
        break
    nom = input("Saisir le nom : ")
    if nom == "FIN":
        break
    matricule = int(input("Saisir le numéro de matricule : ")) 
    infos = (prenom,nom,matricule)
    liste.append(infos)
print(liste)