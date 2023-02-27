from django.urls import path
from .views import HomeView, AboutUsView, CareersView, SearchCareersView, EmailSubscriptionView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('careers/', CareersView.as_view(), name='careers'),
    path('search/', SearchCareersView.as_view(), name='search_vacancy'),
    path('email/', EmailSubscriptionView.as_view(), name='email_subscription'),
]
