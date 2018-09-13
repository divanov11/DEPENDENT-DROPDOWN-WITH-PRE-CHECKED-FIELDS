from rest_framework import serializers
from app.models import *

class TestSerializer(serializers.ModelSerializer):
	class Meta:
		model = LabTest
		fields = ['id','name']