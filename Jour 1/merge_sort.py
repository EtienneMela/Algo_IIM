# TRI PAR FUSION
# Basé sur la technique algorithmique diviser pour régner. 
# L'opération principale de l'algorithme est la fusion, qui consiste à réunir deux listes triées en une seule
import time, sys

def tri_fusion(tableau):
    comparaisons = 0
    if len(tableau) > 1:
        comparaisons += 1
        millieu = len(tableau) // 2
        gauche = tableau[:millieu]
        droite = tableau[millieu:]

        tri_fusion(gauche)
        tri_fusion(droite)

        i = 0
        j = 0
        k = 0
        
        while i < len(gauche) and j < len(droite):
            comparaisons += 2
            if gauche[i] < droite[j]:
                comparaisons += 1
                tableau[k] = gauche[i]
                i += 1
            else:
                tableau[k] = droite[j]
                j += 1
            k += 1
        while i < len(gauche):
            comparaisons += 1
            tableau[k] = gauche[i]
            i += 1
            k += 1
        while j < len(droite):
            comparaisons += 1
            tableau[k] = droite[j]
            j += 1
            k += 1
    return comparaisons, tableau

tab = [int(x) for x in sys.argv[1].split(';')]

print("Série: {} ".format(tab))

start_time = time.time()
comp, resultat = tri_fusion(tab)
exec = time.time() - start_time

print("Résultat: {} ".format(resultat))

print("Nb de comparaisons: {} ".format(comp))
print("Temps d'execution: {} secondes".format(exec))
print("Temps d'execution: {} microsecondes".format(exec * 1000000))