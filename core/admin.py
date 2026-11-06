from django.contrib import admin, messages
from django.contrib.auth.models import Group

from .models import ContactMessage, HeaderNav, HitCount, Post, Profile, Project, Skill

admin.site.unregister(Group)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'whatsapp', 'is_active']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'tech', 'is_featured', 'order']
    list_editable = ['is_featured', 'order']
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            return

        if Post.objects.filter(slug=obj.slug).exists():
            self.message_user(
                request,
                f'Project saved, but a post already uses /blogs/{obj.slug}/ so none was added.',
                messages.WARNING,
            )
            return

        cover = obj.cover_card_url
        body = [obj.description]
        if obj.tech:
            body.append(f'Built with {obj.tech} in {obj.year}.')
        if obj.link:
            body.append(f'Live site: {obj.link}')
        body.append(f'More on the project page: {request.build_absolute_uri(obj.get_absolute_url())}')

        Post.objects.create(
            title=obj.title,
            slug=obj.slug,
            excerpt=obj.summary[:220],
            image_url=request.build_absolute_uri(cover) if cover else '',
            body='\n\n'.join(part for part in body if part),
        )
        self.message_user(
            request,
            f'Blog post added at /blogs/{obj.slug}/ — rewrite it any time under Posts.',
        )


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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'is_published']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    readonly_fields = ['name', 'email', 'phone', 'message', 'created_at']
