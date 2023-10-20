print("Ceci est un petit script python pour voir la table de multiplication d'un chiffre donné")

a = int(input("Veuillez rentrer le chiffre de la table de multiplication souhaité : (Appuyez sur 'entrée' pour continuer) "))
b = 1

while(b<11): 
    c = b*a
    print(f"le résultat de {b} x {a} = {c} ")
    b = b+1
