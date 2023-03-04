from django.contrib.auth import get_user


def user(request):
    return {'user': get_user(request)}