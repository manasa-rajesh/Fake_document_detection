from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aadhaar(request):
    return render(request, 'aadhaarcard/aadhaar.html')


