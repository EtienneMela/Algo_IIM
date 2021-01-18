# TRI RAPIDE
# le pivot est placé à la fin (arbitrairement), en l'échangeant avec le dernier élément du sous-tableau ;
# tous les éléments inférieurs au pivot sont placés en début du sous-tableau ;
# le pivot est déplacé à la fin des éléments déplacés.

import sys
import time, sys

start_time = time.time()

i = 0
def quick_sort(tab):
  global i
  if tab == []:
    i = i + 1
    return []
  else:
    i = i + 1
    pivot = tab[0]

    lowest = []
    largest = []
    for x in tab[1:]:
      if x < pivot:
        i = i + 1
        lowest.append(x)
      else:
        i = i + 1
        largest.append(x)

    return quick_sort(lowest) + [pivot] + quick_sort(largest)

tab = [int(x) for x in sys.argv[1].split(';')]
print("Série: {} ".format(tab))
start_time = time.time()
res = quick_sort(tab)
exec = time.time() - start_time


print("Résultat: {} ".format(res))
print("Nb de comparaisons: {} ".format(i))
print("Temps d'execution: {} secondes".format(exec))
print("Temps d'execution: {} microsecondes".format(exec * 1000000))