from django.shortcuts import render
from rest_framework.views import APIView
from mixins.models import Employee
from mixins.serializers import Employeeserializer
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins

class EmployeeListCreateModelMixin(mixins.CreateModelMixin,ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    def post(self,request):
        return self.create(request)

class EmployeeRetrieveUpdateDestroyeModelMixin(mixins.DestroyModelMixin,mixins.UpdateModelMixin,RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    def put(self, request, *args, **kwargs):
        return self.update(request)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request)



