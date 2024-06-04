def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] += 1
        else:
            resultat[bulletin] = 1
    return resultat



def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale



def verifie(tableau):
    # Un tableau vide ou contenant un seul élément est considéré comme trié
    if len(tableau) <= 1:
        return True
    
    # Vérifier que chaque élément est inférieur ou égal au suivant
    for i in range(len(tableau) - 1):
        if tableau[i] > tableau[i + 1]:
            return False
    
    return True