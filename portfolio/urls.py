from django.urls import path
from .views import portfolio, confirmation, about

urlpatterns = [
    path('', portfolio, name='portfolio'),
    path('about', about, name='about'),
    path('confirmation', confirmation, name='confirmation')
]
