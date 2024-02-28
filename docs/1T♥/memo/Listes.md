# Listes

### 1. Creation d'une liste

```py
ma_liste = [element1, element2]
```
### 2. Longeur d'une liste

```py
len(ma_liste)
```
Renverra un entier.

### 3. Présence d'un élément

```py
element in ma_liste
```
Affichera **True** ou **False**. 

### 4. Index d'un élément

```py
ma_liste.index(element)
```
Renverra un entier naturel.

### 5. Accéder aux éléments d'une liste

```py
ma_liste[index]
```
Cette commande renverra l'élément de la liste associé à l'index indiqué.
N'oublions pas que python commence à compter à partir de 0.


### 6. Modifier la valeur d'un élément de liste 

```py
ma_liste[index] = valeur
```
Que l'on peut aussi écrire :
```py
ma_liste[ma_liste.index(element)] = valeur
```

### 7. Ajouter un élément à une liste 

```py
ma_liste.append(element)
```
L'élément sera ajouter à la fin de la liste.

#### Ajouter un élément à un endroit précis de la liste

```py
ma_liste.insert(index, element)
```
### 9. Suppression d'éléments

#### Enlever un élément de la liste 

```py
ma_liste.remove(element)
```

#### Enlever un élément avec son index

```py
ma_liste.pop(index)
```
Si l'index n'est pas indiqué, Python supprimera le dernier élément.

#### Vider une liste

```py
ma_liste.clear()
```

### 12. Concaténer deux listes 

```py 
ma_liste = liste1 + liste2
```

### 13. Etendre une liste

```py
ma_liste.extend(autre_liste)
```
Cette méthode permet d'ajouter les éléments d'une liste à la fin d'une autre au lieu de créer une nouvelle liste combinant les deux.

### 14. Créer une tranche de liste 

```py
ma_liste[1:4]
```
Renverra les éléments d'index 1, 2, 3.

```py
ma_liste[3:]
```
Renverra les élément de l'index 3 jusqu'à la fin de la liste.

```py
ma_liste[:4]
```
Renverra les éléments du début jusqu'à l'index 3.