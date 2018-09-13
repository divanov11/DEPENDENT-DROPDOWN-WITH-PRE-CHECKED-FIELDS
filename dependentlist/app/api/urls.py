from django.urls import path
from . import views

urlpatterns = [
   path('<int:pk>/', views.testsFuel, name="tests_fuel"),
   path('package/<int:pk>/', views.testsPackage, name="tests_package"),


]
