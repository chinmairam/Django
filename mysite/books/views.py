from django.http import HttpResponse

from django.shortcuts import render
# Create your views here.
from django.template.loader import get_template
from datetime import datetime, timedelta


from books.models import Book


def index(request):
    return HttpResponse("Hello, world. You're at the books index.")


def latest_books(request):
    book_list = Book.objects.order_by("-publication_date")[:10]
    return render(request, 'latest_books.html', {'book_list': book_list})


def iftag(request):
    return render(request, 'iftag.html', {"today_is_weekend": "4"})


def logicaloprs(request):
    return render(request, 'logicaloprs.html', {"athlete_list": ["a","b","c"], "coach_list": ["e", "f", "g"]})
