from math import gcd

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : 
        - 
        POST : 
        - la fraction est automatiquement simplifiée dés sa création

        Raises : 
        - ValueError: si dénominateur == 0 
        """
        
        

    @property
    def num(self):
        return self._num
        
    @property
    def den(self):
        return self._den

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : 
        - Aucune

        POST : 
        - Retourne une chaine au format "numérateur/dénominateur"
        
        Raises:
        - Aucune
        
        """

        
        

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : 
        - Aucun
        POST : 
        - Retourne une réprensatation textuelle de la forme réduite d'une fraction 

        Raises:
        - Aucune
        """
        
        

    
# ------------------ Operators overloading ------------------

    def __add__(self, other: 'Fraction'):
        """Overloading of the + operator for fractions

        PRE : 
        - 
        
        POST : 
        - Retourne une nouvelle fraction simplifiée.

        Raises :
        - TypeError : Si `other` n'est pas une instance de Fraction. 
         
        """

        


    def __sub__(self, other: 'Fraction'):
        """Overloading of the - operator for fractions

        PRE : 
        - 

        POST : 
        - Retourne une nouvelle fraction simplifiée.
        
        Raises :
        - TypeError : Si `other` n'est pas une instance de Fraction.
        
        """
        

    def __mul__(self, other: 'Fraction'):
        """Overloading of the * operator for fractions

        PRE : 
        - 

        POST :
        - Retourne une nouvelle fraction simplifiée.

        Raises :
        - TypeError : Si `other` n'est pas une instance de Fraction.
        """
        


    def __truediv__(self, other: 'Fraction'):
        """Overloading of the / operator for fractions

        PRE : 
        - 
        
        POST : 
        - Retourne une nouvelle fraction simplifiée.
        
        Raises :
        - TypeError : Si `other` n'est pas une instance de Fraction.
        - ZeroDivisionError : Si le numérateur de `other` est nul.
        
        """
        
    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : 
        - `self` doit être une fraction valide (numérateur et dénominateur définis, dénominateur ≠ 0).
        

        POST : 
        - Retourne une nouvelle fraction correspondant à self élevée à la puissance other.
        - Si `other == 0`, retourne 1/1.
        - Si `other > 0`, retourne la fraction multipliée par elle-même `other` fois.
        - Si `other < 0`, retourne l'inverse de la fraction élevée à la puissance absolue de `other`.
        RAISES:
        - ValueError : Si `other` n'est pas un entier (type `int`).
        - ZeroDivisionError : Si la fraction est invalide (numérateur 0) et que `other` est négatif.
    
        """

        
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : 
        -

        POST : 
        - Retourne True si les fractions représentent la même valeur.
        - Retourne False si elles sont différentes 

        Raises: 
        - TypeError : retourne False si 'other' n'est pas une fraction
        """
        
        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : 
        - Auncun
        POST : 
        - Retourne un float représentant la valeur décimale de la fraction.
        """

        
        
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)




# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : 
        - Aucun prérequis spécifique.
        POST :
        - Retourne True si la valeur de la fraction est 0, sinon False
        """
        


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : Aucun
        POST : 
        - Retourne True si la fraction est un entier (valeur entière), sinon False.
        """
        

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : Aucun

        POST : 
        - Retourne True si la valeur absolue de la fraction est inférieure à 1, sinon False.
 
        """
        

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : 
        - La fraction doit être réduite à sa forme irréductible (par la classe elle-même).

        POST : 
        - Retourne True si le numérateur est égal à 1, sinon False.
        
        """

        
        

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : 
        - 

        POST : 
        - Retourne True si la valeur absolue de la différence entre les fractions est une fraction unitaire, sinon False.

        RAISES:
        - TypeError si `other` n'est pas une instance de `Fraction`.
        """

        