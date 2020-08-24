from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Date = models.DateTimeField()
    Description = models.CharField(max_length=500)

    def __str__(self):
        return self.Title 
