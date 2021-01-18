import sys, time

def combsort(array):
    comparaisons = iterations = 0
    gap = len(array)
    swaps = True
    while gap > 1 or swaps:
        comparaisons += 2
        iterations += 1
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(array) - gap):
            comparaisons += 1
            iterations += 1
            j = i + gap
            if array[i] > array[j]:
                comparaisons += 1
                array[i], array[j] = array[j], array[i]
                swaps = True
    return comparaisons, iterations, array

tab = [int(x) for x in sys.argv[1].split(';')]

print("Série: {} ".format(tab))

start_time = time.time()
comp, iter, resultat = combsort(tab)
exec = time.time() - start_time

print("Résultat: {} ".format(resultat))

print("Nb de comparaisons: {} ".format(comp))
print("Nb d'iterations': {} ".format(iter))
print("Temps d'execution': {} secondes".format(exec))
print("Temps d'execution': {} microsecondes".format(exec * 1000000))