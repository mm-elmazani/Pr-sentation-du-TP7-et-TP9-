from tp7_implémentée    import  Fraction
from math import gcd

def main():
    print("=== Tests de la classe Fraction ===\n")
    
    # Test du constructeur
    print("--- Test du constructeur ---")
    f1 = Fraction(3, 4)
    print(f"Fraction f1 créée : {f1}")
    f2 = Fraction(2, 3)
    print(f"Fraction f2 créée : {f2}")

    print("\nTest avec un dénominateur nul :")
    try:
        f_invalid = Fraction(1, 0)  # Doit lever une ValueError
    except ValueError as e:
        print(f"Erreur attrapée : {e}")
    
    # Test de __str__ et as_mixed_number
    print("\n--- Test des représentations textuelles ---")
    print(f"Représentation de f1 : {f1}")
    print(f"f1 en nombre mixte : {f1.as_mixed_number()}")
    f3 = Fraction(7, 3)
    print(f"Représentation de f3 en nombre mixte : {f3.as_mixed_number()}")

    # Test des opérateurs
    print("\n--- Test des opérateurs ---")
    f_add = f1 + f2
    print(f"Addition : {f1} + {f2} = {f_add}")
    
    f_sub = f1 - f2
    print(f"Soustraction : {f1} - {f2} = {f_sub}")
    
    f_mul = f1 * f2
    print(f"Multiplication : {f1} * {f2} = {f_mul}")
    
    f_div = f1 / f2
    print(f"Division : {f1} / {f2} = {f_div}")
    
    f_pow = f1 ** 2
    print(f"Puissance : {f1} ** 2 = {f_pow}")
    
    # Test des vérifications
    print("\n--- Test des vérifications ---")
    print(f"f1.is_zero() : {f1.is_zero()}")
    print(f"f1.is_integer() : {f1.is_integer()}")
    print(f"f3.is_integer() : {f3.is_integer()}")
    print(f"f1.is_proper() : {f1.is_proper()}")
    print(f"f3.is_proper() : {f3.is_proper()}")
    print(f"f1.is_unit() : {f1.is_unit()}")

    # Test de is_adjacent_to
    print("\n--- Test de is_adjacent_to ---")
    f4 = Fraction(1, 2)
    f5 = Fraction(1, 3)
    print(f"{f4} est adjacent à {f5} : {f4.is_adjacent_to(f5)}")
    print(f"{f1} est adjacent à {f2} : {f1.is_adjacent_to(f2)}")

    # Test des erreurs pour les opérateurs
    print("\n--- Test des erreurs ---")
    print("Test de l'addition avec un type invalide :")
    try:
        f_error = f1 + "abc"  # Doit lever une TypeError
    except TypeError as e:
        print(f"Erreur  : {e}")

    print("Test de la division par zéro :")
    try:
        f_error = f1 / Fraction(0, 1)  # Doit lever une ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"Erreur  : {e}")
    
    

if __name__ == '__main__':
    main()
