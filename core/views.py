from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import MovieSpotModel


class Home(TemplateView):
    template_name = 'home.html'

class Search(ListView):
    template_name = 'search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Search, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q')
        print(query)
        if query:
            return MovieSpotModel.objects.search(query)
        else:
            return MovieSpotModel.objects.all()

class MovieDetails(DetailView):
    template_name='movie_details.html'
    model = MovieSpotModel
