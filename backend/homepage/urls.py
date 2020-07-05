from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('api/postcard/', views.postcardListCreate.as_view() ),
]