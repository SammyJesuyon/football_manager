from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('teams/', TeamListView.as_view(), name='teams'),
    path('players/', PlayersListView.as_view(), name='players'),
]