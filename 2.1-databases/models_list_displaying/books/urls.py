from django.urls import path

from books.views import books_view, show_book

urlpatterns = [
    path('', books_view),
    path('<pub_date>/', show_book)
]