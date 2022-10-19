import json
from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
#from django.core.serializers import serialize
from testapp.mixins import SerializeMixin,HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp

    def get(self,request,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resources not available'})
            return self.render_to_http_response(json_data,status=404)
            #return HttpResponse(json_data,content_type='application/json',status=400)

        else:
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)
            # retun HttpResponse(json_data,content_type='application/json' status=200)

    def put(self,request,id):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No Matched Reasource Found, Not possible to perform updation'})
            return self.render_to_http_response(json_data,status=404)

        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        provided_data = json.loads(data)
        original_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        original_data.update(provided_data)
        form= EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps(({'msg':'Resources update successfully'}))
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object_by_id(id)
        if obj is None:
            json_data = json.dumps({'msg': 'No matched record found, Not possible to perform deletion'})
            return self.render_to_http_response(json_data, status=404)
        status, deleted_item = obj.delete()
        if status == 1:
            json_data = json.dumps({'msg': 'Resource Deleted successfully'})
            return self.render_to_http_response(json_data, status=201)
        json_data = json.dumps({'msg': 'unable to delete ...plz try again'})
        return self.render_to_http_response(json_data, status=500)


@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request):
        # json_data = json.dumps({'msg':'This is from post method'})
        # return  self.render_to_http_response(json_data)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send valid json data only'})
            return self.render_to_http_response(json_data,status = 400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps(({'msg':'Resources created successfully'}))
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
# emp_data = {
            #     'eno': emp.eno,
            #     'ename': emp.ename,
            #     'esal': emp.esal,
            #     'eaddr': emp.eaddr
            # }
# json_data = json.dumps(emp_data)