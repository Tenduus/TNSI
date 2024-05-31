def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = ... 
    for bulletin in urne:
        if ...: 
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            ...
    return resultat

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if ... > ... : 
            nmax = ... 
    liste_finale = [ nom for nom in election if ... ] 
    return ... 


-Mémorisation des résultats intermédiaires : Le dictionnaire delannoy_mem est utilisé pour stocker les résultats des appels récursifs déjà calculés.
-Condition de base : Si n ou m est nul (n == 0 ou m == 0), il n'y a qu'un seul chemin possible (en ligne droite), donc le résultat est 1.
-Cas général : Si ni n ni m ne sont nuls, le nombre de chemins allant de (0, 0) à (n, m) est la somme des chemins provenant de (n-1, m), (n, m-1) et (n-1, m-1).
-Mémorisation du résultat : Le résultat est mémorisé dans delannoy_mem pour éviter des calculs redondants futurs.
-Retour du résultat mémorisé : La fonction retourne le résultat mémorisé.