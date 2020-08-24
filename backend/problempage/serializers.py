from rest_framework import serializers
from .models import CpProblem, Cptutorial, pythonProblem, pythontutorial, CPP_Problem, CPP_tutorial, java_problem, java_tutorial

class CpProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpProblem
        fields = ('id', 'topic', 'difficulty_level', 'source', 'prob_name', 'prob_link', 'sol_link')

class CptutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cptutorial
        fields = ('id', 'topic', 'source', 'tut_link')

#######################################################################################
    
class pythonProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = pythonProblem
        fields = ('id', 'topic', 'difficulty_level', 'source', 'prob_name', 'prob_link', 'sol_link')

class pythontutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = pythontutorial
        fields = ('id', 'topic', 'source', 'tut_link')
    
#######################################################################################

class CPPProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPP_Problem
        fields = ('id', 'topic', 'difficulty_level', 'source', 'prob_name', 'prob_link', 'sol_link')

class CPPtutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPP_tutorial
        fields = ('id', 'topic', 'source', 'tut_link')

########################################################################################

class javaProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = java_problem
        fields = ('id', 'topic', 'difficulty_level', 'source', 'prob_name', 'prob_link', 'sol_link')

class javatutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = java_tutorial
        fields = ('id', 'topic', 'source', 'tut_link')


    
