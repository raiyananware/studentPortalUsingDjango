from django.contrib.auth.models import User

def verifyUser(req):
    if req.user.is_authenticated:
        return True
    else:
        return False
