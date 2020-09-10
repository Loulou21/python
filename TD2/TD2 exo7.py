dico = {
    "biscuit":"cookie",
    "clavier":"keyboard",
    "souris":"mouse"
}
dico.update( {"cerveau" : "brain"} )
print(dico)

for i in dico:
    if i == "cerveau":
        trad = dico["cerveau"]
print(trad)

dico2 = {}

for j in dico:
    dico2.update( {dico[j] : j} )

print(dico2)

for k in dico2:
    if k == "brain":
        trad2 = dico2["brain"]

print(trad2)

dico.update( {"cerveau" : ["brain", "qsdg"]} )
print(dico)

dico2['chemin'] = ["path", "way"]
print(dico2)

print(dico2["chemin"][1])

del dico2['chemin']
print(dico2)
print("tonpere")