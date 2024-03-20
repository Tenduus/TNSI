# Dictionnaire

### 1. Créer un dictionnaire

```py
    nom_dico = {clé:val, clé:val}
```
Dans un dictionnaire chaque paire s'écrit sous la forme **clé:valeur**. Chaque clé doit être unqiue dans le dictionnaire. Elle peut être sous la forme d'une chaîne de caractère entre guillemets, une valeur numérique ou un tuple (une sorte de liste non modifiable).

### 2. Accéder aux éléments d'un dictionnaire

```py
    nom_dico[clé]
```

### 3. Tester l'existence d'un clé 

Il est facile de vérifier l'existence d'une clé dans un dictionnaire en écrivant une instruction conditionnelle **if** avec un opérateur **in**.

```py
    if clé in nom_dico:
        action
```

### 4. Ajouter une paire à un dictionnaire 

```py
    nom_dico[clé] = valeur
```
Si l'on écrit la même instruction, mais que la clé existe déjà dans le dictionnaire, la valeur que l'on spécifie remplacera l'ancienne. 

### 5. Enlever un élément d'un dictionnaire

Il existe trois méthode pour enlever un élément dans un dictionnaire : **pop()**, **popitem()**, **del** et **clear()**

##### 1. *Suppression ciblée avec **pop()** et **del**

```py 
    nom_dico.pop(clé)
``` 
Cette méthode permet de supprimer un élément identifié par une clé. Cette méthode en profite aussi pour renvoyer une dèrnière fois la valeur de l'élément qui va disparaître.

```py
    del mon_dico[clé]
```

##### 2. Suppression du dernier élément avec **popitem**

```py
    mon_dico.popitem()
```

Cette méthode renvoie l'entrée complète qu'elle supprime, donc la paire clé-valeur.

##### 3. Supprimer tous les éléments d'un dictionnaire avec **clear**

```py
    mon_dico.clear()
```

### 6. Parcourir un dictionnaire

##### 1. Afficher toutes les clés 

```py
    for clé in nom_dico.keys():
        print(clé)
```

##### 2. Lire toutes les valeurs du dictionnaire

```py
    print(nom_dico[clé])
```

##### 3. Récupérer les clés et les valeurs

```py
    for cle, valeur in nom_dico.items():
        print(cle, valeur)
```

# Dictionnaires imbriqués

```py
    nom_dico = {
        "sous_dico1":{
            clé:valeur,
            clé:valeur
        },
        "sous_dico2:{
            clé:valeur,
            clé:valeur
        }
    }
```
Chaque sous-dictionnaire est défini à la place d'une paire du dictionnaire principal en commençant par son nom, le signe égalet les paires entre deux accolades.

Pour s'y retrouver dans l'utilisation d'un dictionnaire à x niveau, il est indispensable de définir les niveaux de façon cohérente. Il  faut que l'ordre des clés et des valeurs soit le même dans chaque sous-dictionnaire.

### 1. Accéder aux éléments d'un sous-dictionnaire

```py
    print(mon_dico[sous_dico][clé])
```

Il faut d'abord indiqué le nom de la variable correspondant au dictionnaire principal, puis le nom du sous-dictionnaire et la clé entre crochets.

### 2. Ajouter une paire dans un sous-dictionnaire

```py
    mon_dico[sous_dico][clé] = valeur

