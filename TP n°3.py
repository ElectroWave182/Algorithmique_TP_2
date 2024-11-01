# Exercice 1 :

def estMax(x, L):
    n = len(L)
    for i in range(n):
        if x < L[i]:
            return False
    return True

print(estMax(-3, []))

# Sortie : True
# Pourtant, -3 n'est pas le maximum d'une liste vide

def estMax(x, L):
    if L == []:
        return "Erreur : liste vide"
    if not(x in L):
        return False
    for ele in L:
        if x < ele:
            return False
    return True

print(estMax(4, [3, -1, 2]))
print(estMax(0, [0]))
print(estMax(-3, []))


def maxListe(L):
    n = len(L)
    max = L[0]
    for i in range(1, n-1):
        if L[i] < L[i+1]:
            max = L[i+1]
    return max

assert maxListe([3, -1, 2]) == 3, "Erreur : 3 > -1 et 3 > 2"
assert maxListe([0]) == 0, "Erreur : le seul élément d'une liste est son maximum"
assert maxListe([]) == 0, "Erreur : liste vide"

# La fonction d'Alicia n'est donc pas correcte

def maxListe(L):
    n = len(L)
    max = L[0]
    for i in range(n-1):
        if L[i] > max:
            max = L[i]
    return max

assert maxListe([3, -1, 2]) == 3, "Erreur : 3 > -1 et 3 > 2"
assert maxListe([0]) == 0, "Erreur : le seul élément d'une liste est son maximum"
assert maxListe([]) == 0, "Erreur : liste vide"

# La fonction d'Alexandre n'est pas correcte non plus

def maxListe(L):
    if L == []:
        return "Erreur : liste vide"
    max = L[0]
    for ele in L:
        if ele > max:
            max = ele
    return max

assert maxListe([3, -1, 2]) == 3, "Erreur : 3 > -1 et 3 > 2"
assert maxListe([0]) == 0, "Erreur : le seul élément d'une liste est son maximum"
assert maxListe([]) == 0, "Erreur : liste vide"


assert L != [], "Erreur : liste vide"


from random import randint

def listeAléa():
    l = []
    for _ in range(randint(1, 50)):
        l[:] = l[:] + [randint(-50, 50)]
    return l

print(listeAléa())

from random import randint

def estMax(x, L):
    if L == []:
        return "Erreur : liste vide"
    if not(x in L):
        return False
    for ele in L:
        if x < ele:
            return False
    return True

def maxListe(L):
    if L == []:
        return "Erreur : liste vide"
    max = L[0]
    for ele in L:
        if ele > max:
            max = ele
    return max

def listeAléa():
    l = []
    for _ in range(randint(1, 50)):
        l.append([randint(-50, 50)])
    return l

for _ in range(5000):
    l = listeAléa()
    assert estMax(maxListe(l), l), "erreur"


# Exercice 2 :



