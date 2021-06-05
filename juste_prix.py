import random

    # Initalisations:

juste_price = random.randint(1,5)
user_price = 0
print("Veuillez ne pas entrer de valeur au dessus de 10000 (Le juste prix est entre 1-10000)\n")

    # Boucle tant que ce n'est pas égal au bon chiffre:

while juste_price != user_price:

    # Demande du chiffre utilisateur:

    try:
        user_price = int(input("Entrez le chiffre pensé: "))
    except:
        print("Veuillez entrer une valeur valide.")

    # Vérifications:

    if juste_price > user_price:
        print("C'est plus!")
    elif juste_price < user_price:
        print("C'est moins !")
    elif juste_price == user_price:
        print("Bravo c'est gagné !")