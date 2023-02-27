from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import InfoPages, Vacancies


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
    page_id equal 1 because in the PageCategory it has 1st id
    """
    template_name = 'main/about.html'
    information = InfoPages.objects.filter(page_id=1)
    extra_context = {
        'title': 'О нас',
        'informations': information
    }


class CareersView(ListView):
    """
    Careers with us Page
    """
    template_name = 'main/vacancies.html'
    model = Vacancies
    context_object_name = 'vacancies'
    extra_context = {
        'title': 'Карьера с нами',
    }


class SearchCareersView(CareersView):
    """
    Class that is responsible for searching vacancies
    """

    def get_queryset(self):
        words = self.request.GET.get('search-vacancy-engine')
        vacancies_description = Vacancies.objects.filter(description__icontains=words)
        vacancies_title = Vacancies.objects.filter(title__icontains=words)
        return vacancies_description | vacancies_title


class EmailSubscriptionView(TemplateView):
    template_name = 'main/email_subscription.html'
    extra_context = {
        'title': 'Email Подписка'
    }


