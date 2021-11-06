from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def passport(request):
    return render(request, 'passport/passport.html')

