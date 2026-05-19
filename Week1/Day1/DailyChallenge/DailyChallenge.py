#Challenge 1


number = int(input("Entrez un numbre: "))
length = int(input("Entrez une longueur: "))

multiple = []
for i in range(1, length + 1):
    multiple.append(number * i)
print(multiple)



#Challenge 2


mot = input("Entrez un mot: ")
resultat = ""
for lettre in mot:
    if resultat == "" or lettre != resultat[-1]:
        resultat += lettre
print(resultat)
