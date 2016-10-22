# https://github.com/Elliot-Blanchard/MP-01-Polynomes
from math import sqrt
class polynome():
    
    def __init__(self,couples):

        self.couples = couples
        
        self.tab = [0] * 2
        tableau = [0]
        tab = [0]
        for i in range(len(couples)):
            
            if i % 2 == 0:
                tableau.append( couples[i] )

            else:
                tab.append( couples[i] )
        
        self.tab0, self.tab1 = (list(t) for t in zip(*sorted(zip(tab[1:], tableau[1:])))) #Tri joint des 2 listes
        i = 0
        
        self.puissance = [0] * self.tab0[len(self.tab0) - 1]
        for i in range (self.tab0[len(self.tab0) - 1]):
            if i in self.tab0:
                self.puissance[i] = 1
        self.puissance.append(1)

                
        self.coeff = [0]
        t = 0
        for i in range (self.tab0[len(self.tab0) - 1]):
            if self.puissance[i] == 1:
                self.coeff.append(self.tab1[t])
                t = t+1
            else:
                self.coeff.append(0)
        tab2 = self.tab1[-1:]
        self.coeff.append(int(tab2[0]))
        self.coeff = self.coeff[1:]

def afficher(self):
    '''
    Cette fonction affiche le polynome d'une façon compréhensible par l'utilisateur
    '''
    coeff = self.tab1
    puissance = self.tab0
    coeff.reverse()
    puissance.reverse()
    affichage = [0] * len(puissance)
    for i in range(len(puissance)):
        if i != 0:
            if coeff[i] >=0:
                coeff[i] = '+' + str(coeff[i])
        if puissance[i] >=2:
            affichage[i] = "{0}x^{1}".format(coeff[i],puissance[i])
        else:
            if puissance[i] == 1:
                 affichage[i] = "{0}x".format(coeff[i])
            else:
                affichage[i] = str(coeff[i])
    print (''.join(affichage))

def getcoeff (self,nb):
    print (self.tab1[nb])

def getpuissance (self,nb):
    print (self.tab0[nb])

def evalue (self,nb):
    resultat = 0
    for i in range (len(self.tab0)):
        puissance = nb ** self.tab0[i]
        monome = puissance * self.tab1[i]
        resultat = float(resultat) + float(monome)
    print(resultat)

def dmax (self):
    degre = self.tab0
    degre.reverse()
    print (degre[0])
    return degre[0]

def monome (self,nb):
    print(self.tab1[self.tab0.index(nb)])

def somme (poly1,poly2):
    tabsomme = [0] * 2
    tabsomme[0] = poly1.coeff
    tabsomme[1] = poly2.coeff
    somme = list(map(sum, zip(*tabsomme)))
    somme.reverse()
    print (somme)

def difference (poly1,poly2):
    negPoly = [ -x for x in poly2.coeff]
    tabdiff = [0] * 2
    tabdiff[0] = poly1.coeff
    tabdiff[1] = negPoly
    diff = list(map(sum, zip(*tabdiff)))
    diff.reverse()
    print (diff)

def racines (self):
    degre = dmax(self)
    if degre != 2:
        print ("Le polynôme doit être de degré 2 pour pouvoir en calculer les racines")
    else :
        delta = (self.coeff[1]**2) - 4 * self.coeff[0] * self.coeff[2]
        print (delta)
        
    
        
