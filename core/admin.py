from django.contrib import admin
from .models import Profile, Projects, Skills, ContactMessages

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('NAME', 'ROLE', 'EMAIL', 'IS_ACTIVE')
    list_filter = ('IS_ACTIVE',)

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title',)

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

admin.site.site_header = "Abid Kamal Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Your Portfolio Dashboard"
