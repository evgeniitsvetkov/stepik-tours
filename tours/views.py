from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'tours/index.html')


class DepartureView(View):
    def get(self, request, departure):
        return render(request, 'tours/departure.html')


class TourView(View):
    def get(self, request, tour_id):
        return render(request, 'tours/tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')
