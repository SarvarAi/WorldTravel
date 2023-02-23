from django.shortcuts import render
from django.views.generic import TemplateView
from .models import InfoPages


# Create your views here.


class HomeView(TemplateView):
    """
    Home page class
    """
    template_name = 'main/index.html'
    extra_context = {
        'title': 'WorldTravel'
    }


class AboutUsView(TemplateView):
    """
    About Us page
    """
    template_name = 'main/about.html'
    information = InfoPages.objects.filter(page_id=1)
    extra_context = {
        'title': 'О нас',
        'informations': information
    }
