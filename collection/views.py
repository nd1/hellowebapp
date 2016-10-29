from django.shortcuts import render


def index(request):
    # this is my new view
    return render(request, 'index.html')
