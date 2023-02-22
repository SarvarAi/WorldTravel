from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomeView(TemplateView):
    """
    Home page class
    """
    template_name = 'main/index.html'
    context = {
        'title': 'WorldTravel'
    }


class AboutUsView(TemplateView):
    """
    About Us page
    """
    template_name = 'main/about.html'


