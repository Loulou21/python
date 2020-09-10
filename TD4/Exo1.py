from math import pi

def surf_cercle(r=1):
    formule = pi*(r*r)
    return formule

print(surf_cercle())

def vol_boite(longueur=None, largeur=None, hauteur=None):
    if largeur is None and hauteur is None:
        formule = longueur * longueur * longueur
    elif hauteur is None:
        formule = longueur * longueur * largeur
    else :
        formule = longueur * largeur * hauteur
    return formule

print(vol_boite(4))

def remplacement(c1, c2, ch):
    toto = ch.split(c1)
    print(toto)
    toto.insert(1,c2)
    return (toto[0]+toto[1]+toto[2])   
    

print(remplacement("bc","toto","abcdefg"))

# def remplacement(c1=" ", c2="*", ch=""):
#     ch = ch.replace(c1,c2)
#     return ch

# print(remplacement())
