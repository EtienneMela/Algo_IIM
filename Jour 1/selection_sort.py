# TRI PAR SELECTION
# rechercher le plus petit élément du tableau, et l'échanger avec l'élément d'indice 0 ;
# rechercher le second plus petit élément du tableau, et l'échanger avec l'élément d'indice 1 ;
# continuer de cette façon jusqu'à ce que le tableau soit entièrement trié.

import sys
import time, sys

start_time = time.time()
arr = sys.argv[1].split(';')

def selection_sort(tab):
  comparaisons = iterations = 0
  n = len(tab)
  for i in range(n):
    iterations = iterations + 1
    min = i
    for j in range(i + 1, n):
      iterations = iterations + 1
      if (tab[min] > tab[j]):
        comparaisons = comparaisons + 1
        min = j
    tab[i], tab[min] = tab[min], tab[i]
  return comparaisons, iterations, tab


tab = [int(x) for x in sys.argv[1].split(';')]

print("Série: {} ".format(tab))

comp, iter, res = selection_sort(tab)

print("Résultat: {} ".format(res))

exec = time.time() - start_time

print("Nb de comparaisons: {} ".format(comp))
print("Nb d'iterations: {} ".format(iter))
print("Temps d'execution: {} secondes".format(exec))
print("Temps d'execution: {} microsecondes".format(exec * 1000000))