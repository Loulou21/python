# nom = input("Saisir le nom : ")
# prenom = input("Saisir le prénom : ")
# matricule = int(input("Saisir le numéro de matricule : ")) 

# tuple1 = (nom, prenom, matricule)
# dico = {nom : tuple1}
# print(dico)

prenom = ""
nom = ""
dico = {}
while 1:
    prenom = input("Saisir le prénom : ")
    if prenom == "FIN":
        break
    nom = input("Saisir le nom : ")
    if nom == "FIN":
        break
    matricule = int(input("Saisir le numéro de matricule : ")) 
    infos = (prenom,nom,matricule)
    dico.update({nom+prenom[0:2] : infos})
    #print("Le nom de l'etudiant est :",nom," ","le prénom est ",dico[nom][1]," le matricule ",dico[nom][2],)
print(dico)

for j in dico:
    # if j == "Obama":
    #     print("Le nom de l'etudiant est :",j," ","le prénom est ",dico[j][0]," le matricule ",dico[j][2],)
    # else:
    #     print("Pas de Obama")
    if dico[j][2] == 12345678:
        print("Le nom de l'etudiant est :",j," ","le prénom est ",dico[j][0]," le matricule ",dico[j][2],)

#il ne peut pas y avoir 2 index identiques
