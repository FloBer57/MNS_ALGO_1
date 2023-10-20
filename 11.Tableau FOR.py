print("Ceci est un petit script python pour voir la table de multiplication d'un chiffre donné")

a = int(input("Veuillez rentrer le chiffre de la table de multiplication souhaité : (Appuyez sur 'entrée' pour continuer) "))

for i in range(0,11): 
    c = i*a
    print(f"le résultat de {i} x {a} = {c} ")
