from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def driving(request):
    return render(request, 'drivinglicense/driving.html')

