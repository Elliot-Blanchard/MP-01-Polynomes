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
    '''
    Cette fonction renvoie le coefficient du monôme de degré nb appartenant au polynôme self
    '''
    print (self.tab1[nb])

def getpuissance (self,nb):
    '''
    Cette fonction renvoie la puissance du monôme de degré nb appartenant au polynôme self
    '''
    print (self.tab0[nb])

def evalue (self,nb):
    '''
    Cette fonction affiche l'image du nombre nb par le polynôme self
    '''
    resultat = 0
    for i in range (len(self.tab0)):
        puissance = nb ** self.tab0[i]
        monome = puissance * self.tab1[i]
        resultat = float(resultat) + float(monome)
    print(resultat)

def dmax (self):
    '''
    Cette fonction renvoie le degré du polynôme self
    '''
    degre = self.tab0
    degre.reverse()
    return degre[0]

def monome (self,n):
    '''
    Cette fonction affiche le monôme de rang n dans le polynôme
    '''
    print(self.tab1[self.tab0.index(nb)])

def somme (poly1,poly2):
    '''
    Cette fonction affiche le résultat de la somme des deux polynômes poly1 et poly2
    '''
    tabsomme = [0] * 2
    tabsomme[0] = poly1.coeff
    tabsomme[1] = poly2.coeff
    tabsomme[0].reverse()
    tabsomme[1].reverse()
    if len(tabsomme[0]) < len(tabsomme[1]):
        for i in range (len(tabsomme[1]) - len(tabsomme[0])):
            tabsomme[0].insert(0, 0)
        tab = poly2.tab0
    else:
        for i in range (len(tabsomme[0]) - len(tabsomme[1])):
            tabsomme[1].insert(0, 0)
        tab = poly1.tab0
    somme = list(map(sum, zip(*tabsomme)))
    resultat = polynome(couples(somme,tab))
    afficher(resultat)

def difference (poly1,poly2):
    '''
    Cette fonction affiche le résultat de la différence des deux polynômes poly1 et poly2
    '''
    negPoly = [ -x for x in poly2.coeff]
    tabdiff = [0] * 2
    tabdiff[0] = poly1.coeff
    tabdiff[1] = negPoly
    tabdiff[0].reverse()
    tabdiff[1].reverse()
    if len(tabdiff[0]) < len(tabdiff[1]):
        for i in range (len(tabdiff[1]) - len(tabdiff[0])):
            tabdiff[0].insert(0, 0)
        tab = poly2.tab0
    else:
        for i in range (len(tabdiff[0]) - len(tabdiff[1])):
            tabdiff[1].insert(0, 0)
        tab = poly1.tab0
    diff = list(map(sum, zip(*tabdiff)))
    resultat = polynome(couples(diff,tab))
    afficher(resultat)

def racines (self):
    '''
    Cette fonction affiche les racines du polynôme de degré 2 entré en paramètre
    '''
    degre = dmax(self)
    if degre != 2:
        print ("Le polynôme doit être de degré 2 pour pouvoir en calculer les racines")
    else :
        delta = (self.coeff[1]**2) - 4 * self.coeff[0] * self.coeff[2]
        print ('Delta =',delta)
        self.racine1 = ((-self.coeff[1])- sqrt(delta))/(2*self.coeff[0])
        self.racine2 = ((-self.coeff[1])+ sqrt(delta))/(2*self.coeff[0])
        print ('racine 1 =',self.racine1)
        print ('racine 2 =',self.racine2)

def derivee (self):
    '''
    Cette fonction affiche la dérivée du polynôme self
    '''
    dcoeff = [0]*len(self.tab0)
    dpuissance = [0]*len(self.tab0)
    for i in range (len(self.tab0)):
        dcoeff[i] = self.tab1[i] * self.tab0[i]
        dpuissance[i] = self.tab0[i] - 1
    self.derivee = couples(dcoeff[1:],dpuissance[1:])
    derivee = polynome(self.derivee)
    afficher(derivee)

def couples (coeff,puissances):
    couples = [0] * (len(puissances) * 2)
    return sum(zip(coeff, puissances+[0]), ())

def aide():
    print ("Afin de créer un polynôme, vous devez taper le nom du polynôme, suivi per les couples coefficient/puissance qui le définissent, comme nom_du_poly = polynome([c1,p1,c2,p2,etc...])")
    print ("Exemple : Poly = polynome ([-3,2,1,1,2,0]) créera le polynôme -3x²+x+2")
    print ("les autres commandes sont: \n afficher \n getcoeff \n getpuissance \n evalue \n dmax \n monome \n somme \n difference \n racines \n derivee")
    print ("tapez la commande help() puis entrez le nom de la commande en paramètre afin d'en apprendre plus sur une de ces commandes \n Exemple: help(afficher) vous donnera plus d'informations sur la commande afficher")
    print("Pour afficher cette aide à nouveau, tapez aide()")
    
aide()
