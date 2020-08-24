from django.shortcuts import render
from .models import CpProblem, Cptutorial, pythonProblem, pythontutorial, CPP_Problem, CPP_tutorial, java_problem, java_tutorial
from .serializers import CpProblemSerializer, CptutorialSerializer, pythonProblemSerializer, pythontutorialSerializer, CPPProblemSerializer, CPPtutorialSerializer
from .serializers import javaProblemSerializer, javatutorialSerializer
from rest_framework import generics

class CPproblemListCreate(generics.ListCreateAPIView):
    queryset = CpProblem.objects.all().order_by('id')
    serializer_class = CpProblemSerializer

class CPtutorialListCreate(generics.ListCreateAPIView):
    queryset = Cptutorial.objects.all().order_by('id')
    serializer_class = CptutorialSerializer

########################################################################

class pythonproblemListCreate(generics.ListCreateAPIView):
    queryset = pythonProblem.objects.all().order_by('id')
    serializer_class = pythonProblemSerializer

class pythontutorialListCreate(generics.ListCreateAPIView):
    queryset = pythontutorial.objects.all().order_by('id')
    serializer_class = pythontutorialSerializer

########################################################################
class CPPproblemListCreate(generics.ListCreateAPIView):
    queryset = CPP_Problem.objects.all().order_by('id')
    serializer_class = CPPProblemSerializer

class CPPtutorialListCreate(generics.ListCreateAPIView):
    queryset = CPP_tutorial.objects.all().order_by('id')
    serializer_class = CPPtutorialSerializer


#########################################################################

class javaproblemListCreate(generics.ListCreateAPIView):
    queryset = java_problem.objects.all().order_by('id')
    serializer_class = javaProblemSerializer

class javatutorialListCreate(generics.ListCreateAPIView):
    queryset = java_tutorial.objects.all().order_by('id')
    serializer_class = javatutorialSerializer


