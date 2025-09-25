def is_admin_user(request):
    return {'is_admin': request.user.groups.filter(name='Admin').exists() if request.user.is_authenticated else False}