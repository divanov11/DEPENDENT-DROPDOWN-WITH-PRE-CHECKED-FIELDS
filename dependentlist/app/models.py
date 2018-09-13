from django.db import models

class FuelType(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class LabTest(models.Model):
	name = models.CharField(max_length=200, null=True)
	fuels = models.ManyToManyField(FuelType,  blank=True)
	
	def __str__(self):
		return self.name

class Package(models.Model):
	name = models.CharField(max_length=200, null=True)
	tests = models.ManyToManyField(LabTest,  blank=True)
	
	def __str__(self):
		return self.name

class Sample(models.Model):
	customer = models.CharField(max_length=200, null=True)
	fuel = models.ForeignKey(FuelType, null=True, on_delete = models.CASCADE)
	package = models.ForeignKey(Package, null=True, on_delete = models.CASCADE)
	tests = models.ManyToManyField(LabTest,  blank=True)
	
	def __str__(self):
		return self.customer + ' ' + str(self.id)