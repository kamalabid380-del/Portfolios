from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Project


class PageSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['home', 'work', 'contact']

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    priority = 0.7
    changefreq = 'monthly'

    def items(self):
        return Project.objects.all()
