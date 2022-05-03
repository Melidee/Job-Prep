from django.db import models

class Agent(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

class Lead(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

