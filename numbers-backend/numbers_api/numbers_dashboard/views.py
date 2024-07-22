from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from rest_framework import viewsets, permissions
from rest_framework.renderers import JSONRenderer
from numbers_api.serializers import NumberMSerializer
from numbers_dashboard.models import NumberM


# Create your views here.


@require_GET
def dashboard(request):
    avaiable_numbers = NumberM.objects.filter(enable=True)
    serializer = NumberMSerializer(avaiable_numbers, many=True)
    #return HttpResponse(JSONRenderer().render({"data":serializer.data}))
    return JsonResponse({"data":serializer.data}, safe=False)


class NumberMViewSet(viewsets.ModelViewSet):
    queryset=NumberM.objects.all()
    serializer_class=NumberMSerializer
    # permission_classes = [permissions.IsAuthenticated]
# TO_DO: Permisos en viewset

# TO_DO: Login para ABM de NumberKind
