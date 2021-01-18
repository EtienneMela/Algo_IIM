# README
Exercices d'algorithmique du jour 1 réalisés par : 
- Adrien Bannwarth
- Paartheepan Raveenthiran
- Etienne Mela
> TP 9 sur Discord

## Tri à bulle

Ce tri consite à comparer un élément 1 et un élément 2 consécutifs d'un tableau et de les pérmuter si l'élément 1 est supérieur à l'élément 2. On recommence l'opération jusqu' à ce qu’il n’y ait plus de permutation. 


## Tri par insertion

Ce tri consiste à insérer le premier élément à trier à l'index 1 d'une nouvelle liste. Puis on insére chaque élement à sa bonne place dans la liste dèja triée. Puis on recommence l'opération jusqu' a replacé les éléments de la liste initial.


## Tri Peigne

Ce tri est basé sur le même principe que le tri à bulle à l'exception qu'il compare des éléments plus "lointain" et ne compare pas uniquement les éléments adjacents. Au fur et à mesure des comparaisons, l'algo raccourci progressivement l'intervalle entre les éléments du tableau.


## Tri par selection

Ce tri consiste à trouver la plus petite valeur de la liste et la placer en premier élément de la liste/tableau.  
Dans la cas où le tableau est de taille > 1 on réitère sur les éléments du sous tableau (celui qui exclu le minimum actuel).


## Tri rapide 

Cet algorithme consiste à utiliser une valeur pivot. À savoir la valeur du milieu du résultat.  
Le but est de créer un sous ensemble par rapport à cette valeur pivot constitués des éléments les plus petits à gauche et des plus éléments les plus grands à droite.  

On applique cette même fonction aux deux sous ensemble jusqu'à obtenir un sous ensemble d'une seule valeur.


## Tri shell

Le tri de Shell trie chaque liste d'éléments séparés de n positions chacun avec le tri par insertion. L'algorithme effectue plusieurs fois cette opération en diminuant n jusqu'à n=1 ce qui équivaut à trier tous les éléments ensemble.


## Tri fusion

Dans un premier temps on découpe le tableau en 2 de manière récursive afin de trier les 2 parties avec l'algorithme du tri fusion.  


## Benchmark des algos

Tris stable: 
- Tri par insertion 
- Tri bulle 
- Tri fusion

Tris instable: 
- Tri par séléction 
- Tri peigne 
- Tri Shell 
- Tri rapide

 > Tableau utilisé : "12;22;46;90;8;36;82;27;72;2;38;71;11;75;63"


|Type de tri     |Temps d'Execution (µs)         |Comparaisons                 |Iterations                   |Remarques                    |
|----------------|-------------------------------|-----------------------------|-----------------------------|-----------------------------|
|Tri Rapide      |32                             |84                           |               NA            |pivot définit à l'index 0    |
|Tri Insertion   |24                             |116                          |65                           |                             |
|Tri Bulle       |41                             |170                          |119                          |                             |
|Tri Fusion      |73                             |32                           |               NA            |                             |
|Tri Sélection   |116                            |27                           |120                          |                             |
|Tri Peigne      |56                             |126                          |100                          |                             |
|Tri Shell       |30                             |93                           |65                           |                             |
