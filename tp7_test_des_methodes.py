from tp7_implémentée    import  Fraction

from math import gcd

def main():
    # Test du constructeur et de la représentation textuelle
    print("Test du constructeur et de __str__ :")
    f1 = Fraction(3, 4)
    print(f"f1 = {f1} ")
    
    f2 = Fraction(7, 8)
    print(f"f2 = {f2} ")

    # Test de as_mixed_number
    print("\nTest de as_mixed_number :")
    f3 = Fraction(7, 3)
    print(f"f3 = {f3.as_mixed_number()} ")

    f4 = Fraction(4, 2)
    print(f"f4 = {f4.as_mixed_number()} ")

    # Test des opérateurs (+, -, *, /, **)
    print("\nTest des opérateurs :")
    f5 = f1 + f2
    print(f"f1 + f2 = {f5} ")

    f6 = f2 - f1
    print(f"f2 - f1 = {f6} ")

    f7 = f1 * f2
    print(f"f1 * f2 = {f7} ")

    f8 = f1 / f2
    print(f"f1 / f2 = {f8} ")

    f9 = f1 ** 2
    print(f"f1 ** 2 = {f9} ")

    # Test de __eq__
    print("\nTest de __eq__ :")
    f10 = Fraction(2, 4)
    f11 = Fraction(1, 2)
    print(f"f10 == f11 : {f10 == f11} ")

    # Test des méthodes de vérification (is_zero, is_integer, etc.)
    print("\nTest des méthodes de vérification :")
    print(f"f1.is_zero() : {f1.is_zero()} ")
    print(f"f4.is_integer() : {f4.is_integer()} ")
    print(f"f1.is_proper() : {f1.is_proper()} ")
    print(f"f10.is_unit() : {f10.is_unit()} ")

    # Test de is_adjacent_to
    print("\nTest de is_adjacent_to :")
    f12 = Fraction(1, 2)
    f13 = Fraction(1, 3)
    print(f"f12.is_adjacent_to(f13) : {f12.is_adjacent_to(f13)} ")

if __name__ == '__main__':
    main()
