from django.urls import path
from .views import home_view

appname = "shortener"

urlpatterns = [
    path("", home_view, name="home")
]
