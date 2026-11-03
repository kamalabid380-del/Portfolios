from django.contrib import admin
from django.contrib.auth.models import Group

from .models import ContactMessage, HeaderNav, HitCount, Profile, Project, Skill

admin.site.unregister(Group)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'whatsapp', 'is_active']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'tech', 'is_featured', 'order']
    list_editable = ['is_featured', 'order']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(HeaderNav)
class HeaderNavAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'order', 'is_active']
    list_editable = ['url', 'order', 'is_active']


@admin.register(HitCount)
class HitCountAdmin(admin.ModelAdmin):
    list_display = ['path', 'count']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    readonly_fields = ['name', 'email', 'phone', 'message', 'created_at']
