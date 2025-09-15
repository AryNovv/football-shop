from django.shortcuts import render
from django.db import Model

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495590',
        'name': 'Arya Novalino Pratama',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)


