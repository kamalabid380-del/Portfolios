from django.db import ProgrammingError
from django.db.utils import OperationalError

from .models import Profile


def profile(request):
    try:
        prof = Profile.objects.filter(is_active=True).last()
    except (OperationalError, ProgrammingError):
        prof = None
    return {
        'profile': prof,
        'nav_name': prof.name.upper() if prof else 'PORTFOLIO',
    }
