#Exercice 1

print("Hello world\n" * 4)


#Exercice 2

print((99**3)*8)



#Exercice 3


 >>> 5 < 3 # False (5 n'est pas inférieur à 3)
 >>> 3 == 3 # True  (3 est égal à 3)
 >>> 3 == "3" # False (un int et un str ne sont jamais égaux)
 >>> "3" > 3 # Erreur (on ne peut pas comparer str et int)
 >>> "Hello" == "hello"  # False (majuscule ≠ minuscule)





#Exercice 4

computer_brand = "Dell"
print("I have a " + computer_brand + " computer")


#Exercice 5

name = "KOE"
age = 23
shoe_size = 44
info = f"My name is {name}, I'm {age} years old and my shoe size is {shoe_size}"
print(info)


#Exercice 6

a = 10
b = 5
if a > b:
    print("Hello World")



#Exercice 7


nombre = int((input("Entrer un nombre:")))
if nombre % 2 == 0:
    print(f"{nombre} est un nombre pair")
else: 
    print(f"{nombre} est un nombre impair")


#Exercice 8


mon_nom = "KOE"
nom = input("Quel est votre nom ? ")
if nom == mon_nom:
    print("Joliiiiiiiiieeeeeeeeeeeeeee :) !")
else: 
    print("C'est quel nom ça ? Tchrrrrrrr :(")



#Exercice 9

taille_en_centimettre = int(input("Entrez votre taille en centimètre svp: "))
if taille_en_centimettre >= 145:
    print("Vous êtes assez grand pour monter à cheval !")
else:
    print("Désolé, vous devez encore grandir pour pouvoir monter à cheval !")