from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    def __str__(self): return self.title

class HeaderNav(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    def __str__(self): return self.name
