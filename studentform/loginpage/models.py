from django.db import models


class Login(models.Model):
    registration_num = models.CharField(primary_key=True, max_length=30, null=False, default=None, unique=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email_id = models.EmailField(null=True, unique=True)
    phone_num = models.IntegerField(null=True, unique=True)
    address_id = models.CharField(max_length=220, null=True)
    # country = models.CharField(max_length=30, null=True)


    class Meta:
        managed = True
        db_table = 'LOGIN_CREDENTIALS'