"""withrestpro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/',views.EmployeeListAPIView.as_view()),
    path('post/',views.EmployeeCreateAPIView.as_view()),
    path('read/<int:pk>/',views.EmployeeRetrieveAPIView.as_view()),
    path('update/<int:id>/',views.EmployeeUpdateAPIView.as_view()),
    path('delete/<int:id>/',views.EmployeeDestoryAPIView.as_view()),
    path('get-post/',views.EmployeeListCreateAPIView.as_view()),
    path('read-update/<int:id>/',views.EmployeeRetrieveUpdateAPIView.as_view()),
    path('read-delete/<int:id>/',views.EmployeeRetrieveDestroyeAPIView.as_view()),
    path('read-update-delete/<int:id>/',views.EmployeeRetrieveUpdateDestroyAPIView.as_view())

]
