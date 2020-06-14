from django.urls import path
from .views import (
    Home,
    Search,
    MovieDetails,
)

app_name = 'core'

urlpatterns = [
    path('', Home.as_view()),
    path('moviespot/', Search.as_view(), name='query'),
    path('moviespot/<int:pk>/',MovieDetails.as_view(), name='details'),
]
