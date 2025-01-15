from django.db import models

# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=100)  # Table ka naam
    capacity = models.IntegerField()         # Number of people possible
    is_available = models.BooleanField(default=True)  
    
    def __str__(self):
        return self.name

