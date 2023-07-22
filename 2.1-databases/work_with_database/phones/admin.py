from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'release_date', 'slug']
    prepopulated_fields = {'slug': ['name']}
    list_filter = ['id', 'price', 'release_date']
