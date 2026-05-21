#Exercice 1 : Saisir un mois et afficher la saison correspondante   

mois = int(input("Entrez un mois (de 1 à 12) :  "))

if 3 <= mois <= 5:
    print("Spring")
elif 6 <= mois <= 8:
    print("Summer")
elif 9 <= mois <= 11:
    print("Autumn")
elif mois == 12 or 1 <= mois <= 2:
    print("Winter")
else:
    print("Mois invalide, veuillez entrer un nombre entre 1 et 12.")




#Exercice 2

