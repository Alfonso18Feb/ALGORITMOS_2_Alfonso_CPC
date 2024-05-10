#Recursividad para calcular el factorial de un número.
from functools import *
@lru_cache(maxsize=25)# memoriza los numeros que pongas
def factorial(n):
    """Calcula el factorial de un número dado.
    
    Parameters
    ----------
    n : int
        Número entero al que se le calculará el factorial.
        
    Returns
    -------
    int
        El factorial del número dado.
        
    Example
    -------
    factorial(5)
    120
    """
    #Código a realizar.
    # if n<0:
    #     raise ValueError('tiene que ser mayor que 0')
    if n==0:#si es 0 devueve 1
        return 1

    else:
        return n*factorial(n-1)# si no n multiplica por esta funcion recursiva n-1 veces hasta llegar a 0


def main():
    print("=================================================================.")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================.")
    print("The factorial of 5 is: ", factorial(5))

if __name__ == "__main__":
    main()
    