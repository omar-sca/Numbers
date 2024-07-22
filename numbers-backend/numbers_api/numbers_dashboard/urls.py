from django.urls import path, include
from numbers_dashboard import views
from rest_framework.routers import DefaultRouter

router_edit=DefaultRouter()
router_edit.register('', views.NumberMViewSet, basename='editar')

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('edit/', include(router_edit.urls)),
]
