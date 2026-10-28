from django.db import ProgrammingError
from django.db.utils import OperationalError

from .models import Profile


def profile(request):
    try:
        return {'profile': Profile.objects.filter(is_active=True).last()}
    except (OperationalError, ProgrammingError):
        return {'profile': None}
