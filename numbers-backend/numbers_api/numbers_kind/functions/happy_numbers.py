import doctest

def agregar_a_dic(lista, dic, valor):
    for e in lista:
        dic[e] = valor


def happy_number(n, l_recorrido, d_calculados, valor_final=1, potencia=2):
    """
    Función que calcula si el número n es un número felíz; ya sea porque la suma de sus dígitos elevados al cuadrado da
    1, porque ya fue calculado anteriormente o porque se ingresó en un loop.

    :param n: int: número a determinar si es número feliz
    :param l_recorrido: list: recorrido de números. Desde número inicial hasta n. Se usa para verificar si se ingreso en un loop
    :param d_calculados: dict: diccionario de números felices ya calculados anteriormente
    :param valor_final: int: valor por el cual un número es feliz (por defecto 1)
    :param potencia: int: potencia que se le aplica a cada dígito (por defecto 2)
    :return: bool: dependiendo si n es un número feliz o no lo es

    >>> happy_number(7,[],{})
    True
    >>> happy_number(8,[],{})
    False
    """

    suma = 0
    l_recorrido.append(n)
    for d in str(n):
        suma += int(d)**potencia
    if suma == valor_final:
        agregar_a_dic(l_recorrido, d_calculados, True)
        return True
    elif suma in d_calculados:
        agregar_a_dic(l_recorrido, d_calculados, d_calculados[suma])
        return d_calculados[suma]
    elif suma in l_recorrido:
        agregar_a_dic(l_recorrido, d_calculados, False)
        return False
    else:
        return happy_number(suma, l_recorrido, d_calculados)


def main_happy_numbers(cant, diccionario_calculados={}):
    """

    :param cant: int: cantidad de números felices a devolver.
    :param diccionario_calculados: dict: diccionario de números felices ya calculados anteriormente
    :return: list: lista de números felices

    >>> main_happy_numbers(10)
    [1, 7, 10, 13, 19, 23, 28, 31, 32, 44]
    """

    n = 1
    lista_happy_numbers = []
    while len(lista_happy_numbers) != cant:
        lista_aux = []
        if happy_number(n, lista_aux, diccionario_calculados):
            lista_happy_numbers.append(n)
        n += 1
    return(lista_happy_numbers)



if __name__ == '__main__':
    doctest.testmod()

