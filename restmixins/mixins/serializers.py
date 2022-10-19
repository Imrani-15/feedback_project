from rest_framework.serializers import ModelSerializer
from mixins.models import Employee

class Employeeserializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'