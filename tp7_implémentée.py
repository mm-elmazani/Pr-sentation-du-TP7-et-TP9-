from math import gcd

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        
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
        

        return f"{self.num}/{self.den}" 
        

    def as_mixed_number(self) :
        
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
        

        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        
        new_num = (self.num * other.den + self.den * other.num)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)


    def __sub__(self, other: 'Fraction'):
        
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        
        new_num = (self.num * other.den - self.den * other.num)
        new_den = self.den * other.den

        common_divisor = gcd(new_num, new_den)
        new_num //= common_divisor
        new_den //= common_divisor

        return Fraction(new_num, new_den)

    def __mul__(self, other: 'Fraction'):
        
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        
        new_num = self.num * other.num
        new_den = self.den * other.den

        return Fraction(new_num, new_den)


    def __truediv__(self, other: 'Fraction'):
        
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        
        if other.num == 0:
            raise ZeroDivisionError("Division par zéro impossible.")

        new_num = self.num * other.den
        new_den = self.den * other.num

        return Fraction(new_num, new_den)
    def __pow__(self, other):
        

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
        
        if not isinstance(other, Fraction):
            return False
        

        return self.num * other.den == self.den * other.num
        
    def __float__(self) :
        

        return self.num / self.den
        
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)




# ------------------ Properties checking  ------------------

    def is_zero(self):
        
        return self.num == 0


    def is_integer(self):
        
        return self.num % self.den == 0

    def is_proper(self):
        
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        

        return self.num == 1
        

    def is_adjacent_to(self, other) :
        

        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
    
        # Ramener les fractions au même dénominateur
        lcm_den = (self.den * other.den) // gcd(self.den, other.den)  # Calcul du plus petit commun multiple
        num1 = self.num * (lcm_den // self.den)
        num2 = other.num * (lcm_den // other.den)

        # Vérifier si les numérateurs diffèrent de 1
        return abs(num1 - num2) == 1