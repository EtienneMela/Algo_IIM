import time, sys

def insertionSort(array):
    comparaisons = iterations = 0
    for i in range(1, len(array)):
        comparaisons += 1
        iterations += 1 
        currentValue = array[i] 
        currentPosition = i
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            comparaisons += 2
            iterations += 1
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1
        array[currentPosition] = currentValue
    return comparaisons, iterations, array


tab = [int(x) for x in sys.argv[1].split(';')]

print("Série: {} ".format(tab))

start_time = time.time()
comp, iter, resultat = insertionSort(tab)
exec = time.time() - start_time

print("Résultat: {} ".format(resultat))

print("Nb de comparaisons: {} ".format(comp))
print("Nb d'iterations': {} ".format(iter))
print("Temps d'execution': {} secondes".format(exec))
print("Temps d'execution': {} microsecondes".format(exec * 1000000))