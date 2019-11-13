from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):
    #put data here
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "The city never sleep"
    dest1.price = 765
    dest1.img = "destination_1.jpg"
    dest1.offer = False

    dest2 = Destination()
    dest2.name = "Mumbai"
    dest2.desc = "The city never sleep"
    dest2.price = 765
    dest2.img = "destination_2.jpg"
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "Mumbai"
    dest3.desc = "The city never sleep"
    dest3.price = 765
    dest3.img = "destination_3.jpg"
    dest3.offer = True

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})


