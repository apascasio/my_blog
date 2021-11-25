#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.

class HelloWord(View):
    def get(self, request):
        data = {
            'name': 'Andres',
            'lastname': 'Pascasio'
        }
        return render(request, 'hello_word.html', context=data)