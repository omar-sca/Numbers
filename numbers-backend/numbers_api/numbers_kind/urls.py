from django.urls import path
from numbers_kind import views


urlpatterns = [
    path('correlativos/<int:amount>/', views.correlativos, name='correlativos'),
    path('primos/<int:amount>/', views.primos, name='primos'),
    path('pares/<int:amount>/', views.pares, name='pares'),
    path('felices/<int:amount>/', views.felices, name='felices'),
    path('impares/<int:amount>/', views.impares, name='impares'),
    path('fibonacci/<int:amount>/', views.s_fibonacci, name='fibonacci'),
    path('lucas/<int:amount>/', views.s_lucas, name='lucas'),
    path('pell/<int:amount>/', views.s_pell, name='pell'),
    path('jacobsthal/<int:amount>/', views.s_jacobsthal, name='jacobsthal'),
    ]
