from django.shortcuts import render
from .models import Book


template = 'books/books_list.html'


def books_view(request):
    books = Book.objects.all()
    context = {'data': books}
    return render(request, template, context)


def show_book(request, pub_date):
    next = None
    previous = None

    books = Book.objects.all()
    book = Book.objects.filter(pub_date=pub_date)
    dates = sorted({str(book.pub_date) for book in books})
    if pub_date in dates:
        date_index = dates.index(pub_date)
        if (date_index + 1) < len(dates):
            next = dates[date_index + 1]
        if (date_index - 1) >= 0:
            previous = dates[date_index - 1]
    print(previous, next)
    context = {
        'data': book,
        'previous': previous,
        'next': next,
    }
    return render(request, template, context)