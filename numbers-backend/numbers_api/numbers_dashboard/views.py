from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from rest_framework import viewsets
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


def edit(request):
    #queryset=NumberM.objects.all(enable=True)
    #serializer_class=serializers.NumberMSerializer
    return HttpResponse("Return desde aplicacion dashboard - view edit")
# TO_DO: ABM de NumberKind
