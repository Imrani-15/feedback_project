from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def emp_data_view(request):
    emp_data = {
        'eno':100,
        'ename':'Ravi',
        'esal':1000,
        'eadd':'Pune'
    }

    resp = '<h1> Employee Number:{} <br> Employee Name:{} <br> Employee Salary:{} <br> Employee Address:{}'.format(emp_data['eno'],
                                                                                                                   emp_data['ename'],emp_data['esal'],emp_data['eadd'])
    return HttpResponse(resp)

from django.http import JsonResponse
def emp_data_jsonview(request):
    emp_data={
        'eno': 200,
        'ename': 'Lavi',
        'esal': 2000,
        'eadd': 'London'
    }

    #json_data = json.dumps(emp_data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(emp_data)