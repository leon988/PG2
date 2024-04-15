from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings
# Create your models here.


MEDIUM = (
    ('ACR', 'Acrylic'),
    ('BOD', 'Body Art / Tattoo'),
    ('CER', 'Ceramics'),
    ('CHA', 'Charcoal'),
    ('COL', 'Collage'),
    ('DIG', 'Digital Art'),
    ('DRW', 'Drawing'),
    ('GLS', 'Glass Art'),
    ('H2O', 'Water Color'),
    ('INK', 'Ink / Sumi-e'),
    ('INS', 'Installation Art'),
    ('LTR', 'Leather Work'),
    ('MIX', 'Mixed Media'),
    ('MOS', 'Mosaic'),
    ('MUR', 'Mural / Graffiti'),
    ('MTL', 'Metal Work'),
    ('OIL', 'Oil Painting'),
    ('PAP', 'Paper Art / Origami'),
    ('PAS', 'Pastel'),
    ('PERF', 'Performance Art'),
    ('PHO', 'Photography'),
    ('PRI', 'Print Making'),
    ('SND', 'Sound Art / Music'),
    ('SCU', 'Sculpture'),
    ('TXT', 'Textile Art / Fiber Arts'),
    ('TYP', 'Typography'),
    ('OTH', 'Other')
)

STYLES = (
    ('ABS', 'Abstract'),
    ('ART', 'Art Nouveau'),
    ('BOT', 'Botanical'),
    ('CLA', 'Classical'),
    ('CON', 'Contemporary'),
    ('CUB', 'Cubism'),
    ('EXP', 'Experimental'),
    ('FOL', 'Paper Folding / Papercraft'),
    ('IMP', 'Impressionism'),
    ('KNI', 'Knit / Crochet'),
    ('MIN', 'Minimalism'),
    ('MUS', 'Music'),
    ('NAR', 'Narrative'),
    ('PIX', 'Pixel Art'),
    ('POP', 'Pop Art'),
    ('POR', 'Portrait'),
    ('POT', 'Porcelain / Stoneware'),
    ('POS', 'Post Modernism'),
    ('REA', 'Realism'),
    ('ROM', 'Romanticism'),
    ('SKE', 'Sketch'),
    ('SOU', 'Interactive Sound Installation'),
    ('STR', 'Street Art'),
    ('SUR', 'Surrealism'),
    ('THE', 'Theatrical'),
    ('THA', 'Thangka'),
    ('TOO', 'Tattoo / Henna'),
    ('QUI', 'Quilting / Weaving'),
    ('VIN', 'Vintage'),
    ('OTH', 'Other'),
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
    date = models.DateField('Creation/Performance Date', default=now)
    price = models.DecimalField('Valuation', max_digits=1000, decimal_places=2)
    style = models.ManyToManyField(Style)
    medium = models.ForeignKey(Medium, on_delete=models.PROTECT)
    description = models.TextField(max_length=750)
    like = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title: {self.title} | User: {self.user.username} | ID: {self.id}'

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
        return f'Comment: {self.comment} | User: {self.user.username} | Date: {self.date}'
    
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

    def __str__(self):
        return f'User: {self.user} | ID: {self.id}'
