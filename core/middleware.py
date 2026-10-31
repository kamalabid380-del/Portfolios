EXCLUDED_PREFIXES = ('/admin', '/static', '/media')


class HitCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.method == 'GET'
            and not request.path.startswith(EXCLUDED_PREFIXES)
            and not request.session.get('counted')
        ):
            from .models import HitCount
            obj, _ = HitCount.objects.get_or_create(path='total')
            HitCount.objects.filter(pk=obj.pk).update(count=obj.count + 1)
            request.session['counted'] = True
        return self.get_response(request)
