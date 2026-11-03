import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

_django_application = get_wsgi_application()

from django.conf import settings  # noqa: E402  (needs the app loaded)
from whitenoise import WhiteNoise  # noqa: E402

application = WhiteNoise(_django_application, root=str(settings.STATIC_ROOT), prefix='static/')
application.add_files(str(settings.MEDIA_ROOT), prefix='media/')
