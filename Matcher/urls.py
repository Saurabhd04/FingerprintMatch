from django.urls import path
from . import views
urlpatterns = [
    path('UserDetails', views.ProfileViews.as_view()),
    path('Thumbs', views.MatchView.as_view()),
]
