from django.contrib import admin

# Register your models here.
from .models import Name

class NameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name_text']}),
        ('Date information', {'fields': ['entry_date']}),
    ]
    list_display = ('name_text', 'entry_date')
    search_fields = ['name_text']
    list_filter = ['entry_date']

admin.site.register(Name,NameAdmin)

