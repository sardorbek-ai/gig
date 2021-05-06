from django.urls import path
from .views import ClientRegistrations, ClientLogin, client_logout

app_name = 'client'

urlpatterns = [
    path('registration/', ClientRegistrations.as_view(), name="registration"),
    path('login/', ClientLogin.as_view(), name="login"),
    path('logout/', client_logout, name="logout"),
]