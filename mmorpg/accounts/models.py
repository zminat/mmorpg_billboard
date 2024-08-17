import uuid
import random

from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class UserVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link_uuid = models.UUIDField(
         default=uuid.uuid4
    )
    code = models.CharField(default=str(random.randint(1000, 9999)), max_length=4, validators=[MinLengthValidator(4)])
