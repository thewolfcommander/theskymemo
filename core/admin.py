from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    This is the Contact Admin for handling of the Contact Model
    """
    list_display = ['id', 'name', 'email', 'added', 'ip_address']
    list_filter = ['added', 'updated']
    search_fields = ['name', 'email']