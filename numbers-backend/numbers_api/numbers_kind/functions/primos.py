import doctest
import itertools


def primo(e, divisor=2):
    """
    Evalia si un numero es o no es primo.
    :param e: int: elemento a evaluar si o no un numero primo.
    :return: bool: 

    >>> primo(7)
    True
    >>> primo(9)
    False
    """

    if divisor >= e:
        return True
    elif e % divisor == 0:
        return False
    else:
        return primo(e, divisor + 1)
        

def _generador(step=1):
    '''
    Generador: devuelve los posibles numeros primos. 
    Se devulve 1,2 y luego todos los impares >= a 3, ya que 2 es el único numero primo par.

    :return: generator: int : posibles numeros primos
    '''
    yield 1
    yield 2
    num = 3
    while True:
        yield num
        num += step


def main_primos(cant):
    """
    :param cant: int: cantidad de números primos a devolver.
    :return: list: lista de números primos

    >>> main_primos(14)
    [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    """
    
    l_n=[]

    for e in itertools.takewhile(lambda _ : len(l_n)<cant, _generador(step=2)):
        if primo(e): l_n.append(e)
    
    return l_n


if __name__ == '__main__':
    doctest.testmod()
