# main/admin.py
from django.contrib import admin
from .models import Contact, Blog

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'markas_soled', 'markas_available', 'update_at', 'created_at', 'location_name')
    list_filter = ('markas_soled', 'markas_available', 'created_at')
    search_fields = ('title', 'content', 'location_name')
    readonly_fields = ('update_at', 'created_at')

    def has_location(self, obj):
        return obj.has_location()
    has_location.boolean = True
    has_location.short_description = 'Has Location'