from django.shortcuts import render
from bureau.models import Person, Bureau

def index(request):
    context = { 'title': 'Qui est où ?',
              'liste': Person.objects.all()}
    return render(request,'bureau/index.html', context)
