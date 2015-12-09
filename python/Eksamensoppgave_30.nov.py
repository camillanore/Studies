# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:23:14 2015

@author: NBCNO1
"""
#3a
import numpy as np

N = 3

y = np.zeros(N+1, int)
for i in range(1, N+1):    
    y[i] = i*y[i-1]
    print i, y[i]
"""Output
1 0
2 0
3 0

Den printer i verdien og den tilhørende y verdien
"""
#3b
N = 4

y = np.zeros(N+1, int)
y[0] = 1
for i in range(1, N+1):
    y[i] = i*y[i-1]
    print i, y[i]
"""Output:
1 1
2 2
3 6
4 24
Sett n til 4, for å få med alle vi ønsker
legge til initialbetingelse y[0] = 1
"""
#3c
#put the program in a python function. Løsning def... return ...
#call the function y_14
# erase print in order to print nothing

def factorial(N): #lagt til funksjon
    y = np.zeros(N+1, int)
    y[0] = 1
    for i in range(1, N+1):
        y[i] = i*y[i-1]
    return y #returnerer arrayen y

y_14 = factorial(14)[-1] #vis at du kan kalle funksjonen riktig

#3d Test function for the python function in c

def test_factorial(): # skal ikke ta inn noen argumenter
# Test some N > 0, here N=5
    expected = 5*4*3*2*1
    computed = factorial(5)[-1] # check final element
    assert expected == computed #standard assert 
    # Test also the special case N=0
    expected = 1 #bedre test om du også tester spesialtilfelle
    computed = factorial(0)
    assert expected == computed
#her heltall bruker assert. flyttall så bruker vi tol, altså toleranse
# setter standard 10e-16  (maskinpresisjon)  
"""
IKKE LIKE MYE GJENBRUK I ÅR SOM I FJOR
"""

#Exercise 4
#bruk av dictionaries (brukt mye på forelesning)
#nøkkel: potens i 
#tilhørende verdi er koeffisientern før leddet
#nøkkel 8 verdi 20
#dictionary som input
#returnerer verdien av polynomet 
#Clue her: formel for en sum
# clue 2: i for løkka: bruke over dictionaries
#itererer over nøklene i dictionariesene
#p(i) vil være verdiene

def polyeval(x, p):
    s = 0 # summation variable
    for i in p: #for løkke for å evaluere hver sum til det ikke er flere ledd
        s += p[i]*x**i #clue: riktig bruk av dictionaries
    return s

# Simpler implementation
def polyeval(x, p):
    return sum(p[i]*x**i for i in p) 

# exercise 4b. Kan se oppgave 1d) 
def polyadd(p, q):
    r = p.copy() # result. # skal være en kopi 
    for i in q:  # alle nøklene i polynom for andre argument
        if i in r: # hvis den finnes, da er dette polynomet i begge koeffisientene
            r[i] += q[i] # så skal den legges til
        else: #hvis den ikke finnes i r
            r[i] = q[i] #så skal vi lage et nytt element
    return r

# dette er metoden for å legge sammen to polynomer

# Exercise 5 
# ska representeres av en klasse
# Reuse functions polyeval and polyadd
class Poly:
    def __init__(self, p):
        self.coeff = p
    def __call__(self, x):
        return polyeval(x, self.coeff)
    def __add__(self, other): # kan bruke sub og andre spesialmetoder
        result_dict = polyadd(self.coeff, other.coeff)
    return Poly(result_dict)
# legge sammen to instanser i en klasse
# implementere add funksjonen i klassen din
# other; så går dette bra.
# Hint: bruk add funksjon, må huske dette. 
"""
navnet er knyttet til ulike funksjoner i class.
alle klasse metoder tar self + noe annet.
må ha riktig antall input argumenter.
coeff er en atributt i klassen poly.
alle instanser har en coeff atributt.
"""
# Exercise 6
# 
"""
Starter med det vi vet: om du ikke kommer lengre
forklar hva du tenker å gjøre
prøv deg på en slags sum ++
class Poly:
    ...
    def diff(self)
    .
    .
    .
    return Poly(..)
"""
class Poly:
    #...
    def diff(self): #
        r = {} # resulting polynomial. tom dictionary som skal ta vare på resultatet
        for i in self.coeff: #gå gjennom alle nøkler i self.coeff
            if i != 0: # bruker formelen som er oppgitt i oppgaven
                r[i-1] = i*self.coeff[i] # bare tar med def til den deriverte
        return Poly(r)
# Clue: hver nøkkel i gir nøkkel i-1 i den deriverte
# spesialtilfelle: i = 0 , så er det konstantleddet og deriverte er lik null
"""Eksempel:
om self.coeff = x + x**2
så blir dictionaryen:
{1:2, 2:1}
r[i-1]:
    r[0] = 1 *1 = 1
    r[1] = 2 * 1 = 2
Får da en ny nøkkel r = {0:1, 1:2}
r = 1 + 2x
"""
# Exercise 7
# a) skriv en subklasse av superklassen for å
#implementere rk2
""" Ser at i solve har vi en self.advance som ikke finnes noe annet
sted enn i class ForwardEuler, hvor vi har def advance(self)
"""
# Clue: lese og forstå vedlegget
# skal implementere vår egen advance funksjon
#må oversette de tre matematiske kodene til lovlig python kode

from ODESolver import ODESolver

def advance(self):  
    y, f, k, x = self.y, self.f, self.k, self.x # gjør dette for å slippe å skrive self hver gang
    dx = x[k+1] - x[k]
    k1 = dx*f(y[k], x[k])
    k2 = dx*f(y[k] + 0.5*k1, x[k] + 0.5*dx)
    return y[k] + k2

# b) skriv testfunksjon om rk2
# hint
# initialiserer 

def test_RK2():
    """Linear solution should be exactly reproduced."""
    def y(x):
        return 2*x + 3
    def f(y, x):
        return 2 + (y - (2*x+3))**2
    solver = RK2(f)
    solver.set_initial_condition(y(0)) # for å få satt initialbetingelsene
    computed_y, x = solver.solve([0, 1, 2, 3])
    expected_y = y(x) # sender med array x får ut analytiske verdier
    
    import numpy as np
    diff = np.abs(expected_y - computed_y).max() # kunne brukt for løkke for å sammenlikne
    tol = 1E-15
    assert diff < tol

# hovedpoenget her er å skjønne ODESolver og vite hva du skal bruke 
# og hva du må lage nytt i denne oppgaven.