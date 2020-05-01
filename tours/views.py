from random import sample

from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render
from django.views import View

import tours.data as data


class MainView(View):
    def get(self, request):
        sample_tours = sample(data.tours.items(), 6)

        return render(request, 'tours/index.html', {'title': data.title,
                                                    'subtitle': data.subtitle,
                                                    'description': data.description,
                                                    'departures': data.departures,
                                                    'sample_tours': sample_tours})


class DepartureView(View):
    def get(self, request, departure):
        if departure not in data.departures:
            raise Http404

        tours_from_departure = {}
        for tour_id, tour in data.tours.items():
            if tour['departure'] == departure:
                tours_from_departure[tour_id] = tour

        return render(request, 'tours/departure.html', {'title': data.title,
                                                        'departures': data.departures,
                                                        'departure': departure,
                                                        'tours_from_departure': tours_from_departure})


class TourView(View):
    def get(self, request, tour_id):
        if tour_id not in data.tours:
            raise Http404

        tour_data = data.tours[tour_id]
        return render(request, 'tours/tour.html', {'title': data.title,
                                                   'departures': data.departures,
                                                   'tour': tour_data})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')
