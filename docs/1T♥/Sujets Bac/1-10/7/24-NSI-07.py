def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer 
        # où placer la valeur à ranger
        j = i 
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]: 
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = valeur_insertion

def  gb_vers_entier(tab):
    entier = 0
    n = len(tab)
    for i in range(n):
        if tab[i]:
            entier += 2 ** (n - 1 - i)
    return entier