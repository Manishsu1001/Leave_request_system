from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class leaves(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    desc = models.TextField()
    status = models.CharField(max_length=2)
    fromdate = models.DateField()
    todate = models.DateField()

