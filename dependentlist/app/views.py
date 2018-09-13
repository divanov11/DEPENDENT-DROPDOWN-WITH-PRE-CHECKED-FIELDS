from django.shortcuts import render
from .forms import *
from .models import *


def createSample(request):
	form = SifForm()
	context = {'form':form}
	return render(request, 'app/create_sample.html', context)
