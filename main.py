# - PSEUDOCODE BINGO -

# ********************************************
# carte_bingo : Fonction qui génère visuellement la carte bingo du joueur.
# ********************************************
# Entrées :
# Sorties :
# ********************************************
# --Début--
#
#
# --Fin--
#
#
#
# ********************************************
# tirage_chiffre : Fonction qui tire un chiffre et vérifie si elle est dans la carte du joueur.
# ************** Variables *******************
# Entrées : chiffre_choisi (float), liste_actuelle (ls)
# Sorties : liste_actuelle (ls)
# ********************************************
# --Début--
#
# --Fin--
#
#
# ********************************************
# vérification_carte : Fonction qui vérifie si la combinaison de chiffres gagne.
# ************** Variables *******************
# Entrées :
# Sorties :
# ********************************************
# --Début--
#
# --Fin--
#
#
# ********************************************
# Programme Principal
# ************** Variables *******************
# Entrées : nom (str), prenom (str), Nb_essais (int), score (float), chiffre_choisi (int) liste_actuelle (ls
# Intermédiaires :
# Sorties :
# ********************************************
# --Début--
#
#
# --Fin--

import random

def creer_carte_bingo():
    nombres = random.sample(range(1, 76), 25)
    grille = [nombres[i * 5:(i + 1) * 5] for i in range(5)]
    grille[2][2] = "FREE"
    return grille

def afficher_carte_bingo(grille):
    print("\n  B    I    N    G    O")
    print("-" * 25)
    for ligne in grille:
        # Formate chaque élément sur 4 caractères pour aligner les colonnes
        print(" ".join(f"{str(case):^4}" for case in ligne))
    print("-" * 25)

def marquer_numero(grille, numero):
    for i in range(5):
        for j in range(5):
            if grille[i][j] == numero:
                grille[i][j] = "X"
                return True
    return False