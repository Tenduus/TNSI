def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = "" 
    while a > 0 : 
        bin_a = str(a % 2) + bin_a 
        a = a // 2  
    return bin_a


def nb_repetitions(elt, tab):

    compteur = 0
    for element in tab:
        if element == elt:
            compteur += 1
    return compteur