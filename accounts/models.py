import uuid
from django.contrib import auth
from django.db import models


auth.signals.user_logged_in.disconnect(auth.models.update_last_login)


class User(models.Model):
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True
    
    @classmethod
    def find_sharee(cls, email):
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return False
        else:
            return True
        
    
class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=40)
