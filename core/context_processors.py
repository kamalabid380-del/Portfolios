from django.db import ProgrammingError
from django.db.utils import OperationalError

from .models import HitCount, Profile


def profile(request):
    try:
        prof = Profile.objects.filter(is_active=True).last()
    except (OperationalError, ProgrammingError):
        prof = None
    return {
        'profile': prof,
        'nav_name': prof.name.upper() if prof else 'PORTFOLIO',
    }


def hit_count(request):
    try:
        total = HitCount.objects.filter(path='total').values_list('count', flat=True).first() or 0
    except (OperationalError, ProgrammingError):
        total = 0
    return {'hit_count': total}
