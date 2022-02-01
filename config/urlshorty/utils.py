from django.conf import settings
from django.urls import path
from .views import home_view, redirect_url_view
from random import choice
from string import ascii_letters, digits

appname = "shortener"

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAIABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAIABLE_CHARS):
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )


def create_shortened_url(model_instance):
    random_code = create_random_code()

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        return create_shortened_url(model_instance)

    return random_code


urlpatterns = [
    path('', home_view, name='home'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]
