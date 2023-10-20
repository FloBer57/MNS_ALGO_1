print("Ceci est un petit script python pour trouver calculer le prix TTC à partir du prix HT")

prixHorsTaxe = float(input("Veuillez rentrer le prix HT : (Appuyez sur 'entrée' pour continuer) "))

prixTtc = prixHorsTaxe * 1.20

print(f"Pour le prix HT {prixHorsTaxe}, le prix TTC est de : {prixTtc}")