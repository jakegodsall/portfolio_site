from django.urls import path
from .views import portfolio, confirmation

urlpatterns = [
    path('', portfolio, name='portfolio'),
    path('confirmation', confirmation, name='confirmation')
]
