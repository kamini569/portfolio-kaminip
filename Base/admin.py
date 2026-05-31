from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'message', 'date')
    search_fields = ('name', 'email', 'number')
    list_filter = ('date',)
    ordering = ('-date',)

admin.site.register(Contact, ContactAdmin)