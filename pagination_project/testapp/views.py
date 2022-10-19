from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import Employeeserializer
from rest_framework import generics
from testapp.pagination import Mypagination, Myoffset

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    search_fields = ('eno','ename')
    ordering_fields = ('eno','ename')
    # search_fields = ('^eno',) # It return all records where no contains number
    # search_fields = ('=eno',) # It return all records where no exactly equal to number
    #pagination_class =  Myoffset
    # def get_queryset(self):
    #     qs = Employee.objects.all()
    #     name = self.request.GET.get('ename')
    #     if name is not None:
    #         qs  = qs.filter(ename__icontains=name)
    #     return qs