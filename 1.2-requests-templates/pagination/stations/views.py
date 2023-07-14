from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(BUS_STATION_CSV, 'r', encoding='UTF-8') as csvfile:
        info = csv.DictReader(csvfile, delimiter=',')
        data = [value for value in info]
    chosen_page = int(request.GET.get('page', 1))
    paginator = Paginator(data, 10)
    page = paginator.get_page(chosen_page)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
