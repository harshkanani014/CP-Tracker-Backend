from django.shortcuts import render
from .models import CpProblem, Cptutorial, pythonProblem, pythontutorial, CPP_Problem, CPP_tutorial
from .serializers import CpProblemSerializer, CptutorialSerializer, pythonProblemSerializer, pythontutorialSerializer, CPPProblemSerializer, CPPtutorialSerializer
from rest_framework import generics

class CPproblemListCreate(generics.ListCreateAPIView):
    queryset = CpProblem.objects.all()
    serializer_class = CpProblemSerializer

class CPtutorialListCreate(generics.ListCreateAPIView):
    queryset = Cptutorial.objects.all()
    serializer_class = CptutorialSerializer

########################################################################

class pythonproblemListCreate(generics.ListCreateAPIView):
    queryset = pythonProblem.objects.all()
    serializer_class = pythonProblemSerializer

class pythontutorialListCreate(generics.ListCreateAPIView):
    queryset = pythontutorial.objects.all()
    serializer_class = pythontutorialSerializer

########################################################################
class CPPproblemListCreate(generics.ListCreateAPIView):
    queryset = CPP_Problem.objects.all()
    serializer_class = CPPProblemSerializer

class CPPtutorialListCreate(generics.ListCreateAPIView):
    queryset = CPP_tutorial.objects.all()
    serializer_class = CPPtutorialSerializer


