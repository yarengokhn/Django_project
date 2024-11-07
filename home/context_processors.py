
from .models import Settings


def settings(request):
    settings = Settings.objects.first()
     # return {'settings': Setings.objects.get(pk=1)}
    if settings:
        return {'settings': settings}