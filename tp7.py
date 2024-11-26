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
        - le dénominateur ne doit pas être égal à zéro
        POST : 
        - la fraction est automatiquement simplifiée dés sa création

        Raises : 
        - ValueError: si dénominateur == 0 
        """
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro.")

        self._den = den
        self._num = num
        

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

        return f"{self.num}/{self.den}" 
        

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : ?
        POST : 
        - Retourne une réprensatation textuelle de la forme réduite d'une fraction 

        Raises:
        - Aucune
        """
        # Calcul de la partie entière
        integer_part = self.num // self.den

        # Calcul de la fraction propre (reste)
        remainder = self.num % self.den

        # Si la fraction est exactement un entier
        if remainder == 0:
            return f"{integer_part}"

        # Si la partie entière est nulle
        if integer_part == 0:
            return f"{remainder}/{self.den}"

        # Sinon, combinaison de la partie entière et de la fraction propre
        return f"{integer_part} {remainder}/{self.den}"
        

    
# ------------------ Operators overloading ------------------

    def __add__(self, other: 'Fraction'):
        """Overloading of the + operator for fractions

        PRE : 
        - `other` doit être une instance de Fraction.
        
        POST : 
        - Retourne une nouvelle fraction simplifiée.

        Raises :
        - TypeError : Si `other` n'est pas une instance de Fraction. 
         
        """

        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        
        new_num = (self.num * other.den + self.den * other.num)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)


    def __sub__(self, other: 'Fraction'):
        """Overloading of the - operator for fractions

        PRE : 
        - `other` doit être une instance de Fraction.

        POST : 
        - Retourne une nouvelle fraction simplifiée.
        
        Raises :
        - TypeError : Si `other` n'est pas une instance de Fraction.
        
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        
        new_num = (self.num * other.den - self.den * other.num)
        new_den = self.den * other.den

        common_divisor = gcd(new_num, new_den)
        new_num //= common_divisor
        new_den //= common_divisor

        return Fraction(new_num, new_den)

    def __mul__(self, other: 'Fraction'):
        """Overloading of the * operator for fractions

        PRE : 
        - `other` doit être une instance de Fraction.

        POST :
        - Retourne une nouvelle fraction simplifiée.

        Raises :
        - TypeError : Si `other` n'est pas une instance de Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        
        new_num = self.num * other.num
        new_den = self.den * other.den

        return Fraction(new_num, new_den)


    def __truediv__(self, other: 'Fraction'):
        """Overloading of the / operator for fractions

        PRE : 
        - `other` doit être une instance de Fraction.
        - Le numérateur de `other` ne doit pas être nul.
        
        POST : 
        - Retourne une nouvelle fraction simplifiée.
        
        Raises :
        - TypeError : Si `other` n'est pas une instance de Fraction.
        - ZeroDivisionError : Si le numérateur de `other` est nul.
        
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        
        if other.num == 0:
            raise ZeroDivisionError("Division par zéro impossible.")

        new_num = self.num * other.den
        new_den = self.den * other.num

        return Fraction(new_num, new_den)
    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : 
        - `self` doit être une fraction valide (numérateur et dénominateur définis, dénominateur ≠ 0).
        - `other` doit être un entier (type `int`).

        POST : 
        - Retourne une nouvelle fraction correspondant à self élevée à la puissance other.
        - Si `other == 0`, retourne 1/1.
        - Si `other > 0`, retourne la fraction multipliée par elle-même `other` fois.
        - Si `other < 0`, retourne l'inverse de la fraction élevée à la puissance absolue de `other`.
        RAISES:
        - ValueError : Si `other` n'est pas un entier (type `int`).
        - ZeroDivisionError : Si la fraction est invalide (numérateur 0) et que `other` est négatif.
    
        """

        if not isinstance(other, int):
            raise ValueError("L'exposant (other) doit être un entier.")
        
        if self.num == 0 and other < 0:
            raise ZeroDivisionError("Impossible d'élever une fraction nulle à une puissance négative.")

        if other == 0:
            return Fraction(1, 1) 

        if other > 0:
            return Fraction(self.num ** other, self.den ** other)
        
        if other < 0:
            return Fraction(self.den ** abs(other), self.num ** abs(other))
        
        return Fraction(self.den ** other, self.num ** other)
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : 
        - `other` doit être une instance de Fraction.

        POST : 
        - Retourne True si les fractions représentent la même valeur.
        - Retourne False si elles sont différentes 

        Raises: 
        - TypeError : retourne False si 'other' n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            return False
        

        return self.num * other.den == self.den * other.num
        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : ?
        POST : 
        - Retourne un float représentant la valeur décimale de la fraction.
        """

        return self.num / self.den
        
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)




# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : 
        - Aucun prérequis spécifique.
        POST :
        - Retourne True si la valeur de la fraction est 0, sinon False
        """
        return self.num == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : Aucun
        POST : 
        - Retourne True si la fraction est un entier (valeur entière), sinon False.
        """
        return self.num % self.den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : Aucun
        POST : 
        - Retourne True si la valeur absolue de la fraction est inférieure à 1, sinon False.
 
        """
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : 
        - La fraction doit être réduite à sa forme irréductible (par la classe elle-même).

        POST : 
        - Retourne True si le numérateur est égal à 1, sinon False.
        
        """

        return self.num == 1
        

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : 
        - `other` doit être une instance de `Fraction`.

        POST : 
        - Retourne True si la valeur absolue de la différence entre les fractions est une fraction unitaire, sinon False.

        RAISES:
        - TypeError si `other` n'est pas une instance de `Fraction`.
        """

        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
    
        # Ramener les fractions au même dénominateur
        lcm_den = (self.den * other.den) // gcd(self.den, other.den)  # Calcul du plus petit commun multiple
        num1 = self.num * (lcm_den // self.den)
        num2 = other.num * (lcm_den // other.den)

        # Vérifier si les numérateurs diffèrent de 1
        return abs(num1 - num2) == 1