from django.db import models

class Auth(models.Model):
    id= models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username + '-' + self.email
    
    @property
    def is_authenticated(self):
        return True
    
