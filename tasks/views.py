# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tasks.models import customer, taskDetails, joiningTask
from tasks.serializers import customerSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def customerList(request):

    if request.method == 'GET':
        customers = customer.objects.all()
        serializer=customerSerializer(customers,many=True )
        return JsonResponse(serializer.data, safe=False)

    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer = customerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def customerDetails(request,pk):
    try:
        customer1 = customer.objects.get(pk=pk)
    except customer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = customerSerializer(customer1)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = customerSerializer(customer1, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=204)






