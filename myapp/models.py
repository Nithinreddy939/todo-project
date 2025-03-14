from django.db import models

# Create your models here.

class todoitem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField( max_length=50)
    updated_at = models.DateField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.title