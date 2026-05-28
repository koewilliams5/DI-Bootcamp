

try:
    
    date = input("votre date de naissance (précisez le format, par exemple : DD/MM/YYYY) :")
    
    dates = date.split("/")

    day = int(dates[0])
    month = int(dates[1])
    year = int(dates[2])

    year_birn = 2025 - year

    print(f"  ___{year_birn}___")
    print("   |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")
except ValueError :
    print("Entrez une valeur valide")