from django.db import models


class logininfo(models.Model):
    name = models.CharField('Full Name', max_length=50)
    email = models.EmailField('Email ID', max_length=200)
    password = models.CharField('Password', max_length=500)

    def __str__(self):
        return self.name
