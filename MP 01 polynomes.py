# https://github.com/Elliot-Blanchard/MP-01-Polynomes

##1ere méthode(1 seule liste/vecteur)
##class Polynome():
##
##    def __init__(self,couples):
##
##        self.couples = couples
##        
##        self.coeff = [0] * len ( couples )
##        for i in range (len ( couples ) ) :
##            if i % 2 == 0 :
##                self.coeff[i] = 0
##            else:
##                self.coeff[i] = couples[ i - 1 ]
##
##        self.puissance = [0] * len ( couples )
##        for i in range (len ( couples)):
##            if self.coeff[i] == 0:
##                self.puissance[i] = 0
##            else:
##                self.puissance[i] = 1
##
##def afficher(self):
##    
##    afficher(nom du polynôme)
##    Cette fonction affiche le polynome d'une façon compréhensible par l'utilisateur
##    
##    print ( "({0}x^{1})+({2}x^{3})+({4}x^{5})".format(self.couples[0],self.couples[1],self.couples[2],self.couples[3],self.couples[4],self.couples[5]))
##

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
    affichage = [0] * len(puissance)
    for i in range(len(puissance)):
        affichage[i] = "{0}x^{1}".format(self.coeff[i],self.puissance[i])
    print (join(affichage))
    
    
