print("Ceci est un petit script python pour calculer le prix d'une commande")

a = float(input("Veuillez rentrer la moyenne de français ( /20) : (Appuyez sur 'entrée' pour continuer) "))
b = float(input("Veuillez rentrer la moyenne de math ( /20) : (Appuyez sur 'entrée' pour continuer) "))
c = float(input("Veuillez rentrer la moyenne de géométrie ( /20) : (Appuyez sur 'entrée' pour continuer) "))
d = float(input("Veuillez rentrer la moyenne d'informatique ( /20) : (Appuyez sur 'entrée' pour continuer) "))

moyenne = a+b+c+d
Calc = moyenne/4

print("le résultat est",Calc,"/20")