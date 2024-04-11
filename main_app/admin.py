from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


from .models import Art, Medium, Style, Comment, Profile
# Register your models here.
admin.site.register(Art)
admin.site.register(Medium)
admin.site.register(Style)
admin.site.register(Comment)
admin.site.register(Profile)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)





# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model