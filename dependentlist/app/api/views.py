from app.models import *
from django.http import JsonResponse
from . serializers import *

def testsFuel(request, pk):
	tests = LabTest.objects.filter(fuels=pk)
	serializer = TestSerializer(tests, many=True)
	return JsonResponse(serializer.data, safe=False)

def testsPackage(request, pk):
	package = Package.objects.get(id=pk)
	tests = package.tests
	serializer = TestSerializer(tests, many=True)
	return JsonResponse(serializer.data, safe=False)