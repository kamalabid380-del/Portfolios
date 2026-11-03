from django.contrib import admin
from .models import HeaderNav

@admin.register(HeaderNav)
class HeaderNavAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)