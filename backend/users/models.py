from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='profile')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    about = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_pics', default='default.png')
    #cover_image = models.ImageField(upload_to='avatars', default='avatars/cover.png')
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    username = models.CharField(
        'username',
        max_length=50,
        unique=True,
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    gender = models.CharField(max_length=20)
    resume = models.FileField(upload_to ='uploads/', blank=True, null=True) 
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "gender", "first_name", "last_name"]

    def __unicode__(self):
        return self.email

    def _str_(self):
        return self.user.username