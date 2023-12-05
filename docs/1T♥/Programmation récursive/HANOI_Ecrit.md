# Les tours de Hanoï
![kesaco](./images/Hanoi_0.png)
<!-- #### Rappels Pile/File -->
![ex_1-2](./images/Hanoi_ex_1-2.png)
<!-- #### Schémas de principe -->
![ex3](./images/Hanoi_ex3.png)
![ex4](./images/Hanoi_ex4.png)

<div style="page-break-after: always;"></div>

## Programmation en Python

![ex5](./images/Hanoi_ex5.png)

```python
def sommet(pile) :
    if est_vide(pile):
        raise IndexError("pile vide")
    else :
        sommet_valeur = depiler(pile)
        empiler(pile, sommet_valeur)
    return sommet-valeur




```
<div style="page-break-after: always;"></div>

![ex6](./images/Hanoi_ex6.png)

```python
def deplacer(origine, cible) :
    element = depiler(origine)
    empiler(cible, element)






```
![ex7](./images/Hanoi_ex7.png)

```python
deplacer(p0, p1)
deplacer(p0, p2)
deplacer(p1, p2)


```
![ex8-1](./images/Hanoi_ex8-1.png)

```python
deplacer(origine, cible)
```
![ex8-2](./images/Hanoi_ex8-2.png)

```python
resoudre(n-1, p0, p1)
deplacer(p0, p2)
resoudre(n-1, p1, p2)


```
![ex9-1](./images/Hanoi_ex9-1.png)
```
nb_etapes(1) = 1
```
![ex9-2](./images/Hanoi_ex9-2.png)
```
nb_etapes(n) = 2*(n-1)+1
```
![ex9-3](./images/Hanoi_ex9-3.png)
```python
def nb_etapes(n) :
    if n==1 :
        return 1 
    else : 
        return 2*nb_etapes(n-1)+1







```
