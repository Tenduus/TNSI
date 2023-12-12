def creer_pile():
    '''Renvoie une pile vide'''
    pile = []
    return []

def est_vide(pile):
    '''Renvoie un booléen, True si la pile est vide et False sinon'''
    return not pile

def empiler(pile, element):
    '''Empile element au sommet de pile'''
    pile.append(element)
    
def depiler(pile):
    '''Renvoie et enlève la valeur du sommet de pile'''
    assert not est_vide(pile), "Pile vide"
    return pile.pop()

def sommet(pile):
    
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    if est_vide(pile):
        raise IndexError("pile vide")
    else :
        sommet_valeur = depiler(pile)
        empiler(pile, sommet_valeur)
    return sommet_valeur

def mettre_disques(pile, n):
    '''met des disques de taille n à 1 sur la pile'''
    assert n >= 1, "Error 404"
    while n > 0:
        empiler(pile, n)
        n -= 1
    return pile

def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    return [ mettre_disques(creer_pile(), n), creer_pile(), creer_pile()]