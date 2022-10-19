from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.serializers import NameSerializer

# Create your views here.
class TestAPIView(APIView):
    def get(self,request):
        colors = ['red','yellow','pink']
        return Response({'msg':'Happy New year','colors':colors})

    def post(self,request):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'hello {}, happy new year'.format(name)
            return Response ({'msg':msg})
        else:
            return Response(serializer.errors,status=404)
    def put(self,request):
        return Response ({'msg':'This response from put method of APImethod'})

    def patch(self,request):
        return Response ({'msg':'This response from patch method of APImethod'})

    def delete(self,request):
        return Response ({'msg':'This response from delete method of APImethod'})




from rest_framework.viewsets import ViewSet
class TestViewSet(ViewSet):
    def list(self,request):
        colors = ['yellow','pink','pinky']
        return Response ({'msg':'happy ponal','colors':colors})

    def create(self,request):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'hello {}, happy new year'.format(name)
            return Response({'msg': msg})
        else:
            return Response(serializer.errors, status=404)

    def retrieve(self,request,pk=None):
        return Response({'msg':'This response from retrieve method from Viewset'})

    def update(self,request,pk=None):
        return Response({'msg':'This response from update method from Viewset'})

    def partial_update(self,request,pk=None):
        return Response({'msg':'This response from partial_update method from Viewset'})

    def destroy(self,request,pk=None):
        return Response({'msg':'This response from destroy method from Viewset'})
