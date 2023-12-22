def background(couleur : str = 'black') :
    '''
    Rafraichit la scène avec un fond de la couleur
    'couleur' passée en paramètre et fixée sur `black` par défaut
    Préconditions :
    - couleur (str) : une chaine de caractères définissant une couleur HTML valide
    '''
    s.clear()
    s.fill_rect(0, 0, 600, 400)
    s.fill_style = couleur 