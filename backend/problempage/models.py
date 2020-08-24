from django.db import models

# Create your models here.

# 1 . MODEL FOR COMPETITIVE PROGRAMMING TRACK
class CpProblem(models.Model):
    id = models.IntegerField(primary_key = True, unique= True)
    topic = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=100)
    source = models.CharField(max_length=100)  # for example hackerank, codechef
    prob_name = models.CharField(max_length=1000)   #problem name
    prob_link = models.CharField(max_length=1000)   #problem link
    sol_link = models.CharField(max_length=1000)     #sol_link

class Cptutorial(models.Model):
    id = models.IntegerField(primary_key = True, unique= True)
    topic = models.CharField(max_length=100)
    source = models.CharField(max_length=1000)
    tut_link = models.CharField(max_length=1000)


############################################################
# 2 . MODEL FOR PYTHON  TRACK
class pythonProblem(models.Model):
    id = models.IntegerField(primary_key = True, unique= True)
    topic = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=100)
    source = models.CharField(max_length=100)  # for example hackerank, codechef
    prob_name = models.CharField(max_length=1000)   #problem name
    prob_link = models.CharField(max_length=1000)   #problem link
    sol_link = models.CharField(max_length=1000)     #sol_link

class pythontutorial(models.Model):
    id = models.IntegerField(primary_key = True, unique= True)
    topic = models.CharField(max_length=100)
    source = models.CharField(max_length=1000)
    tut_link = models.CharField(max_length=1000)


############################################################
# 3 . MODEL FOR CPP  TRACK
class CPP_Problem(models.Model):
    id = models.IntegerField(primary_key = True, unique= True)
    topic = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=100)
    source = models.CharField(max_length=100)  # for example hackerank, codechef
    prob_name = models.CharField(max_length=1000)   #problem name
    prob_link = models.CharField(max_length=1000)   #problem link
    sol_link = models.CharField(max_length=1000)     #sol_link

class CPP_tutorial(models.Model):
    id = models.IntegerField(primary_key = True, unique= True)
    topic = models.CharField(max_length=100)
    source = models.CharField(max_length=1000)
    tut_link = models.CharField(max_length=1000)

#########################################################
# 4. MODEL FOR JAVA TRACK

class java_problem(models.Model):
    id = models.IntegerField(primary_key = True, unique= True)
    topic = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=100)
    source = models.CharField(max_length=100)  # for example hackerank, codechef
    prob_name = models.CharField(max_length=1000)   #problem name
    prob_link = models.CharField(max_length=1000)   #problem link
    sol_link = models.CharField(max_length=1000)     #sol_link


class java_tutorial(models.Model):
    id = models.IntegerField(primary_key = True, unique= True)
    topic = models.CharField(max_length=100)
    source = models.CharField(max_length=1000)
    tut_link = models.CharField(max_length=1000)
