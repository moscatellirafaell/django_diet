from django.db import models

# Create your models here.

class Cliente(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)


class Nutri(Cliente):
    crn = models.CharField(max_length=8)
