from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings
# Create your models here.


MEDIUM = (
    ('DIG','Digital'),
    ('MUR','Mural'),
    ('H2O', 'Water Color'),
    ('PAST', 'Pastel'),
    ('CRY', 'Acrylic'),
    ('OIL', 'Oil'),
    ('INK', 'Ink'),
    ('PRI','Print Making'),
    ('CHA','Charcoal'),
    ('PHO', 'Photography'),
    ('SCU', 'Sculpture'),
    ('MIX', 'Mixed Media'),
    ('COL', 'Collage'),
    ('DRAW', 'Drawing'),
    ('TXT', 'Textile Art'),
    ('CER', 'Ceramics'),
    ('PERM', 'Performance Art'),
    ('INST', 'Installation Art'),
    ('GLASS', 'Glass Art'),
    ('MTL', 'Metal Work'),
    ('LEAT', 'Leather Work'),
    ('PEP', 'Paper Art / Origami'),
    ('MOS', 'Mosaic'),
    ('BOD', 'Body Art / Tattoo'),
    ('SND', 'Sound Art / Music'),
    ('OTH', 'Other')
)

STYLES = (
    ('IMP','Impressionism'),
    ('CUB','Cubism'),
    ('SUR', 'Surrealism'),
    ('REA', 'Realism'),
    ('ABS','Abstract'),
    ('ROM', 'Romanticism'),
    ('ART', 'Art Nouveau'),
    ('POP', 'Pop Art'),
    ('POS','Post Modernism'),
    ('MIN', 'Minimalism'),
    ('CON', 'Contemporary'),
    ('THA', 'Thangka'),
    ('OTH', 'Other')
)

# Model 3: Medium
class Medium(models.Model):
    name = models.CharField(max_length=75, choices=MEDIUM, default=MEDIUM[0][0])

    def __str__(self):
        return self.get_name_display()
        
    def get_absolute_url(self):
        return reverse('mediums_detail', kwargs={'pk': self.id})

# Model 2: Style
class Style(models.Model):
    name = models.CharField(max_length=75, choices=STYLES, default=STYLES[0][0])

    def __str__(self):
        return self.get_name_display()
        
    def get_absolute_url(self):
        return reverse('styles_detail', kwargs={'pk': self.id})

# Model 1: Art
class Art(models.Model):
    title = models.CharField(max_length=75)
    image = models.CharField(max_length=500)
    description = models.TextField(max_length=750)
    date = models.DateField('Art Creation Date', default=now)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    like = models.IntegerField(default=0)
    style = models.ManyToManyField(Style)
    medium = models.ForeignKey(Medium, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.id})'

    def get_absolute_url(self):
        return reverse('arts_detail', kwargs={'pk': self.id})

# Model 4: Comment
class Comment(models.Model):
    date = models.DateField("Comment Posting Date", default=now)
    comment = models.TextField(max_length=280)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, blank=True, null=True)   

    def __str__(self):
        return f'Comment by {self.user.username} on {self.date}'
    
    def get_absolute_url(self):
        return reverse('comments_detail', kwargs={'pk': self.id})
    
    class Meta:
        ordering = ['-date']


# Model "5": Profile (adding to User)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=500, blank=True, null=True)
    bio = models.TextField(max_length=280)
    location = models.CharField(max_length=50, blank=True)

# Model "6": Artwork search
class ArtworkTag(models.Model):
    artwork = models.ForeignKey(Art, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('artwork', 'style', 'medium')