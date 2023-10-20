print("Ceci est un petit script python pour calculer le prix d'une commande")

a = float(input("Veuillez rentrer le prix unitaire du produit : (Appuyez sur 'entrée' pour continuer) "))
b = int(input("Veuillez rentrer la quantité de produit commandé : (Appuyez sur 'entrée' pour continuer) "))
c = float(input("Veuillez rentrer le taux de TVA en pourcentage : ( Appuyez sur 'entrée pour continuer) "))
montantHt = a*b 
remise = montantHt * 0.85 
tva = 1 + c/100
prixTtc = remise*tva

print("le résultat est",prixTtc)