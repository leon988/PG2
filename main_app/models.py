from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.





# Model 1: Art
class Art(models.Model):
    title = models.CharField(max_length=75)
    image = models.CharField(max_length=500)
    description= models.TextField(max_length=750)
    date= models.DateField('Art Creation Date')
    price= models.DecimalField(max_digits=10000, decimal_places=2)
    like= models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def __str__(self):
        return f"{self.XXX()} on {self.date}"
    
    def get_absolute_url(self):
        return reverse('artworks_detail', kwargs={'cat_id': self.id})
    # user fk
    # comment fk
    # style fk
    # medium fk
