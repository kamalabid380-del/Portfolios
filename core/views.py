import logging
import re

from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import ContactMessage, Profile, Project, Skill

logger = logging.getLogger(__name__)


def notify_owner(msg):
    profile = Profile.objects.filter(is_active=True).last()
    recipient = (profile.email if profile else '') or settings.CONTACT_EMAIL
    if not recipient:
        return
    safe_name = ' '.join(msg.name.split())[:80]
    body = (
        f"New enquiry from {safe_name}\n\n"
        f"Name: {msg.name}\n"
        f"Email: {msg.email}\n"
        f"Phone: {msg.phone or 'not given'}\n\n"
        f"{msg.message}\n"
    )
    try:
        mail = EmailMessage(
            f"Portfolio enquiry from {safe_name}",
            body,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            reply_to=[msg.email.strip()],
        )
        mail.send(fail_silently=False)
    except Exception:
        logger.exception('Contact notification email failed')


def home(request):
    return render(request, 'core/home.html', {
        'projects': Project.objects.filter(is_featured=True)[:6],
        'skills': Skill.objects.all(),
    })


def work(request):
    skill = request.GET.get('skill', '').strip()
    projects = Project.objects.all()
    tokens = [t for t in re.split(r'[^A-Za-z0-9+#.]+', skill) if t]
    if tokens:
        match = Q()
        for token in tokens:
            match |= Q(tech__icontains=token)
        projects = projects.filter(match)
    return render(request, 'core/work.html', {
        'projects': projects,
        'active_skill': skill,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'core/project_detail.html', {'project': project})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            msg = ContactMessage.objects.create(
                name=name, email=email, phone=phone, message=message,
            )
            notify_owner(msg)
            return redirect('contact_sent')
    return render(request, 'core/contact.html', {'sent': False})


def contact_sent(request):
    return render(request, 'core/contact.html', {'sent': True})


def robots(request):
    sitemap_url = request.build_absolute_uri('/sitemap.xml')
    return HttpResponse(
        f"User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: {sitemap_url}\n",
        content_type='text/plain',
    )
