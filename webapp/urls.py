from django.urls import path
from . import views

urlpatterns = [
    path('api/data', views.ActivityPeriodsListView.as_view()),
]