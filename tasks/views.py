# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tasks.models import customer, taskDetails, joiningTask
from tasks.serializers import customerSerializer, taskSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def customerList(request):
    #get method
    if request.method == 'GET':
        customers = customer.objects.all()
        serializer=customerSerializer(customers,many=True )
        return JsonResponse(serializer.data, safe=False)

    #post method to the customer database
    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer = customerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def customerDetails(request, pk):
    try:
        # variable to get the particular customer
        customer1 = customer.objects.get(pk=pk)

        # variable to access the tasks associated with the customer1 variable
        tasksTaken = customer1.taskdetails_set.all()

    except customer.DoesNotExist:
        return HttpResponse(status=404)

    #get method to get the tasks associated with a customer as json
    if request.method == 'GET':
        serializer = taskSerializer(tasksTaken, many=True)
        return JsonResponse(serializer.data, safe=False)

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

@csrf_exempt
def taskList(request):

    if request.method == 'GET':
        tasks = taskDetails.objects.all()
        serializer = taskSerializer(tasks,many=True )
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = taskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def taskSpecifics(request, pk):
    try:
        tasker = taskDetails.objects.get(pk=pk)

    except taskDetails.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = taskSerializer(tasker)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = taskSerializer(tasker, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        taskDetails.delete()
        return HttpResponse(status=204)



