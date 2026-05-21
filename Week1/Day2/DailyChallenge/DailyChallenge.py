# Challenge 1 : Letter Index Dictionary

word = input("Enter a word: ")
letter_dict = {}

for index, letter in enumerate(word):
    if letter in letter_dict:
        # Letter already exists, add the index to its list
        letter_dict[letter].append(index)
    else:
        # Letter doesn't exist yet, create a new list
        letter_dict[letter] = [index]

print(letter_dict)



#Challenge 2


items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
basket = []

# Étape 1 : nettoyer le portefeuille
wallet = int(wallet.replace("$", "").replace(",", ""))

# Étape 2 : parcourir les articles
for item, price in items_purchase.items():
    # Nettoyer le prix
    price = int(price.replace("$", "").replace(",", ""))
    
    # Si j'ai assez d'argent
    if wallet >= price:
        basket.append(item)
        wallet = wallet - price  # on déduit le prix

# Afficher le résultat
if basket == []:
    print("Nothing")
else:
    print(sorted(basket))
