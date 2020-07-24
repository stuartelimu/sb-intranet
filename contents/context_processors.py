from django.conf import settings

def get_settings(request):
    """return settings for smtp"""
    
    return {
        'host': settings.EMAIL_HOST,
        'user': settings.EMAIL_HOST_USER,
        'password': settings.EMAIL_HOST_PASSWORD
    }