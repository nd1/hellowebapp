from django.shortcuts import render


def index(request):
    # defining variables
    number = 6
    thing = "Thing name"
    # pass the variable to the view
    return render(request, 'index.html', {
        'number': number,
        'thing': thing, })
