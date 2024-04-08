from django.contrib import admin
from .models import Art, Medium, Style, Comment
# Register your models here.
admin.site.register(Art)
admin.site.register(Medium)
admin.site.register(Style)
admin.site.register(Comment)