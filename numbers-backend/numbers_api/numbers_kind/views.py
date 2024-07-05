from django.http import JsonResponse
import json
from functools import wraps
from numbers_kind.functions.happy_numbers import main_happy_numbers
from numbers_kind.functions.primos import main_primos
from numbers_kind.functions.sucesiones import main_fibonacci, main_lucas, main_pell, main_jacobsthal

# Create your views here.


#Decorador
def numbers_list_response(func):
    '''
    Decorator:
    retrun: JsonResponse with ListNumber requested  
    '''
    # con @wraps(func) la devolucion del decorador conserva el nombre de func. Util para que el url dispacher funcione y para conservar el docstring de la funcion
    @wraps(func)
    def wrapper(*args, **kargs):
        if kargs['amount']<1:
            kargs['amount']=1
        # si la lista esta hardcodeada o devuelve mas elementos de los solicitados, la lista se trunca en el decorador
        # n_list=func(*args, **kargs)
        # data_json=json.JSONEncoder().encode(n_list[:kargs['amount']])
        data_json=json.JSONEncoder().encode(func(*args, **kargs))    
        return JsonResponse({'data':data_json},safe=False)
    return wrapper


def _list_generator(amount, func):
    return [ func(e) for e in range(1, amount+1)]


@numbers_list_response
def correlativos(request, amount):
    return _list_generator(amount, lambda e : e)


@numbers_list_response
def pares(request, amount):
    return _list_generator(amount, lambda e : 2*e)


@numbers_list_response
def impares(request, amount):
    return _list_generator(amount, lambda e : 2*e-1)


@numbers_list_response
def primos(request, amount):
    return main_primos(amount)


@numbers_list_response
def felices(request, amount):
    return main_happy_numbers(amount)


@numbers_list_response
def s_fibonacci(request, amount):
    return main_fibonacci(amount)


@numbers_list_response
def s_lucas(request, amount):
    return main_lucas(amount)


@numbers_list_response
def s_pell(request, amount):
    return main_pell(amount)


@numbers_list_response
def s_jacobsthal(request, amount):
    return main_jacobsthal(amount)

