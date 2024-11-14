from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'vaquero_id')  # Show the user and Vaquero ID in the list view
    search_fields = ('user__username', 'vaquero_id')  # Allow searching by username and Vaquero ID

# Register the Profile model with the custom admin class
admin.site.register(Profile, ProfileAdmin)
