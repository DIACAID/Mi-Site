from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

app_name = "diacdev_app"
def index(request):
    cards = [
        {
            "title": "Card 1",
            "text": "This is the first card",
            "image": "card1.jpg",
        },
        {
            "title": "Card 2",
            "text": "This is the second card",
            "image": "card2.jpg",
        },
        {
            "title": "Card 3",
            "text": "This is the third card",
            "image": "card3.jpg",
        },
        {
            "title": "Card 4",
            "text": "This is the fourth card",
            "image": "card4.jpg",
        },
        {
            "title": "Card 5",
            "text": "This is the fifth card",
            "image": "card5.jpg",
        },
        {
            "title": "Card 6",
            "text": "This is the sexth card",
            "image": "card6.jpg",
        },
    ]
    return render(request, 'diacdev_app/index.html', {'cards': cards})
