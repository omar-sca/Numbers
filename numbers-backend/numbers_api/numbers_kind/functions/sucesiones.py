import doctest


_relacion_de_recurrencia = lambda _p, _q, _list, _index: _p * _list[_index-1] + _q * _list[_index-2]


def _iterador(cant, _list, **kargs):
    for i in range(2, cant):
        _list.append(_relacion_de_recurrencia(**kargs, _list=_list, _index=i))

    return _list


def main_fibonacci(cant :int) -> list:
    """
    :param cant: int: cantidad de elementos de la serie de fibonacci a devolver.
    :return: list: lista con la serie de fibonacci

    >>> main_fibonacci(15)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    """
    
    # _p coeficiente de n-1 ; _q coeficiente de n-2 ; _list: elemntos iniciales de la sucesión
    _fibonacci = { '_list':[0,1],
                    '_p': 1,
                    '_q': 1 }
    
    return _iterador(cant, **_fibonacci )


def main_lucas(cant: int) -> list:
    """
    :param cant: int: cantidad de números de lucas a devolver.
    :return: list: lista de números de lucas

    >>> main_lucas(10)
    [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
    """
    
    #_p coeficiente de n-1 ; _q coeficiente de n-2 ; _list: elemntos iniciales de la sucesión
    _lucas = {  '_list': [2,1],
                '_p': 1,
                '_q': 1 }
    
    return _iterador(cant, **_lucas)


def main_pell(cant: int) -> list:
    """
    :param cant: int: cantidad de números de pell a devolver.
    :return: list: lista de números de pell

    >>> main_pell(10)
    [0, 1, 2, 5, 12, 29, 70, 169, 408, 985]
    """

    # _p coeficiente de n-1 ; _q coeficiente de n-2 ; _list: elemntos iniciales de la sucesión
    _pell = {   '_list': [0,1],
                '_p': 2,
                '_q': 1 }
    
    return _iterador(cant, **_pell)


def main_jacobsthal(cant: int) -> list:
    """
    :param cant: int: cantidad de números de jacobsthal a devolver.
    :return: list: lista de números de jacobsthal

    >>> main_jacobsthal(11)
    [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341]
    """

    # _p coeficiente de n-1 ; _q coeficiente de n-2 ; _list: elemntos iniciales de la sucesión
    _jacobsthal = {   '_list': [0,1],
                    '_p': 1,
                    '_q': 2 }
    
    return _iterador(cant, **_jacobsthal)


if __name__ == '__main__':
    doctest.testmod()
