from django.urls import path
from .views import ClientRegistrations

app_name = 'client'

urlpatterns = [
    path('registration/', ClientRegistrations.as_view(), name="registration")
]