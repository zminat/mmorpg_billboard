from django.contrib.auth.models import User
from django.db import models


class NewUser(User):
    status = models.BooleanField(default=False)
    auth_code = models.CharField(max_length=8)


class Ad():
    pass


class Response():
    pass
