from django.shortcuts import render

def index(request):
  context = { 'title': '*B o n j o u r *',
              'content': 'Bonjour !'}
  return render(request, 
       'bonjour/index.html', context)
