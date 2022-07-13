from django.contrib import admin
from django.urls import path
from personal.views import (
    home_screen_view,
)

from account.views import (
    registration_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('register/', registration_view, name="register"),
]
