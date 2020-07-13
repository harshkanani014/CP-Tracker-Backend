from django.urls import path
from .views import CPproblemListCreate, CPtutorialListCreate, pythonproblemListCreate, pythontutorialListCreate,    CPPproblemListCreate, CPPtutorialListCreate



urlpatterns = [
    path('api/postcard/cp/cp-problem', CPproblemListCreate.as_view()),
    path('api/postcard/cp/cp-tutorial', CPtutorialListCreate.as_view()),
    path('api/postcard/python/python-problem', pythonproblemListCreate.as_view()),
    path('api/postcard/python/python-tutorial', pythontutorialListCreate.as_view()),
    path('api/postcard/CPP/CPP-problem', CPPproblemListCreate.as_view()),
    path('api/postcard/CPP/CPP-tutorial', CPPtutorialListCreate.as_view())
]