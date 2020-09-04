from django.contrib import admin
from .models import Profile # add this

class ProfileAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'completed') # add this

# Register your models here.
admin.site.register(Profile, ProfileAdmin) # add this