# TRI DE SHELL
# Le tri de Shell trie chaque liste d'éléments séparés de n positions chacun avec le tri par insertion. 
# L'algorithme effectue plusieurs fois cette opération en diminuant n jusqu'à n=1 ce qui équivaut à trier tous les éléments ensemble. 

import time, sys

def shell_sort(array):
    comparaisons = iterations = 0
    gap = len(array) // 2
    while gap > 0:
        comparaisons += 1
        iterations += 1
        for i in range(gap, len(array)):
            comparaisons += 1
            iterations += 1
            val = array[i]
            j = i
            while j >= gap and array[j - gap] > val:
                comparaisons += 2
                iterations += 1
                array[j] = array[j - gap]
                j -= gap
            array[j] = val
        gap //= 2
    return comparaisons, iterations, array

tab = [int(x) for x in sys.argv[1].split(';')]


print("Série: {} ".format(tab))

start_time = time.time()
comp, iter, result = shell_sort(tab)
exec = time.time() - start_time

print("Résultat: {} ".format(result))

print("Nb de comparaisons: {} ".format(comp))
print("Nb d'iterations: {} ".format(iter))
print("Temps d'execution: {} secondes".format(exec))
print("Temps d'execution: {} microsecondes".format(exec * 1000000))