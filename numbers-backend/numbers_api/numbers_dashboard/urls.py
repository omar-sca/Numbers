from django.urls import path
from numbers_dashboard import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit, name='edit'),
]
