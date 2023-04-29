from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import  place
from .models import team
# Create your views here.
def ifun(request):
    obj= place.objects.all()
    tm= team.objects.all()
    return render(request,"index.html",{'result' : obj, 'result2' : tm})

