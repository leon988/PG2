from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

MEDIUM = (
    ('Digital'),
    ('Mural'),
    ('Water Color'),
    ('Pastel'),
    ('Acrylic'),
    ('Oil'),
    ('Ink'),
    ('Print Making'),
    ('Charcoal'),
    ('Sumi Ink'),
    ('Photography'),
    ('Sculpture'),
    ('Mix Media'),
    ('Collage'),
    ('Others')
)

STYLES = (
    ('Impressionism'),
    ('Cubism'),
    ('Surrealism'),
    ('Realism'),
    ('Abstract'),
    ('Romanticism'),
    ('Art Nouveau'),
    ('Pop Art'),
    ('Post Modernism'),
    ('Minimalism'),
    ('Contemporary'),
    ('Thangka'),
    ('Others')
)


# Model 3: Medium
class Medium(models.Model):
    name = models.CharField(max_length=75, choices=MEDIUM, default=MEDIUM[0[0]])

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('mediums_detail', kwargs={'art_id': self.id})


# Model 2: Style
class Style(models.Model):
    name = models.CharField(max_length=75, choices=STYLES, default=STYLES[0[0]])

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('styles_detail', kwargs={'art_id': self.id})
    
# Model 1: Art
class Art(models.Model):
    title = models.CharField(max_length=75)
    image = models.CharField(max_length=500)
    description = models.TextField(max_length=750)
    date = models.DateField('Art Creation Date')
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    like = models.IntegerField(default=0)
    style = models.ManyToManyField(Style)
    medium = models.ManyToManyField(Medium)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def __str__(self):
        return f"{self.XXX()} on {self.date}"
    
    def get_absolute_url(self):
        return reverse('artworks_detail', kwargs={'art_id': self.id})
    # user fk


# Model 4: Comment
class Comment(models.Model):
    date = models.DateField()
    comment = models.TextField(max_length=280)

  # Create an art_id FK
    art = models.ForeignKey(Art, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.date}'


    

