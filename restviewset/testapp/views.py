from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import Employeeserializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from testapp.permissions import IsReadOnly,IsGETOrPatch
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from testapp.authentications import CustomAuthentication
# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    #authentication_classes = [JSONWebTokenAuthentication,]
    authentication_classes = [CustomAuthentication]
    #permission_classes = [IsReadOnly,]
    #permission_classes = [IsGETOrPatch, ]
    permission_classes = [IsAuthenticated]