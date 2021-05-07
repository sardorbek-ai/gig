from django.conf import settings as ss




def settings(request):
    return {
        'LANGUAGES': ss.LANGUAGES
    }