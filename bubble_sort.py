import time, sys

def tri_bulle(tableau):
    comparaisons = iterations = 0
    n = len(tableau)
    for i in range(n-1):
        comparaisons += 1
        iterations += 1
        for j in range(0, n-i-1):
            comparaisons += 1
            iterations += 1
            if tableau[j] > tableau[j+1] :
                comparaisons += 1
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
    return comparaisons, iterations, tableau

tab = [int(x) for x in sys.argv[1].split(';')]

print("Série: {} ".format(tab))

start_time = time.time()
comp, iter, resultat = tri_bulle(tab)
exec = time.time() - start_time

print("Résultat: {} ".format(resultat))

print("Nb de comparaisons: {} ".format(comp))
print("Nb d'iterations': {} ".format(iter))
print("Temps d'execution': {} secondes".format(exec))
print("Temps d'execution': {} microsecondes".format(exec * 1000000))