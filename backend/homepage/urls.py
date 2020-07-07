from django.urls import path
from . import views


urlpatterns = [
    path('api/postcard/', views.postcardListCreate.as_view()),
    path('api/postcard/<int:pk>', views.postcarddetail.as_view())
]
