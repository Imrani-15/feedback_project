from testapp.models import Employee
from rest_framework import serializers
class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'