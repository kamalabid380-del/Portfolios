from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150, default="Python & Django Web Developer")
    location = models.CharField(max_length=100, default="Lahore, Pakistan")
    email = models.EmailField()
    bio = models.TextField(help_text="2-3 short paragraphs. Plain text.")
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.CharField(max_length=200, help_text="One line shown on cards and in search results.")
    description = models.TextField(help_text="What you built, how, and the result.")
    cover = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech = models.CharField(max_length=200, blank=True, help_text="e.g. Python, Django, PostgreSQL")
    link = models.URLField(blank=True, help_text="Live site or repository.")
    year = models.PositiveIntegerField(default=2026)
    is_featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-year', 'id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.email}"
