from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin
)
from django.conf import settings


class PUserManager(BaseUserManager):

 def create_user(self, username, user_type, password=None):


      if not username:
            raise ValueError('Users must have an email address or mobile number')

      user = self.model(
            username=username,
            user_type=user_type,
      )
      user.set_password(password)
      user.save(using=self._db)
      return user

 def create_superuser(self, username,user_type, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username,
            password=password,
            user_type=user_type,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class PUser(AbstractBaseUser,PermissionsMixin): 
 username = models.CharField(
        verbose_name='Username, email or mobile',
        max_length=255,
        unique=True,
 )
# mobile= models.CharField(max_length=11) 
 user_type_choices=(
  (1, 'Personel'),
  (2, 'Business'),
  (3, 'Mall'),
 )
 user_type=models.PositiveSmallIntegerField(choices=user_type_choices,default=1)
 avatar = models.ImageField(upload_to='user/avatar')
 qq = models.CharField(max_length=20)
 weibo= models.CharField(max_length=20)
 weixin=models.CharField(max_length=20)
 description= models.CharField(max_length=100)
 logo = models.ImageField(upload_to='business/image')
 haswifi = models.BooleanField(True)
 address = models.CharField(max_length=100)
 mobile = models.CharField(max_length=11)
 tel= models.CharField(max_length=11)
 banner= models.ImageField(upload_to='business/image')
 is_active = models.BooleanField(default=True)
 is_admin = models.BooleanField(default=False)
 is_staff = models.BooleanField(default=False)
 objects =PUserManager()
 REQUIRED_FIELDS = ['user_type']
 USERNAME_FIELD= 'username'
  
 
 def get_full_name(self):
        # The user is identified by their email address
        return self.username

 def get_short_name(self):
        # The user is identified by their email address
        return self.username

 def __unicode__(self):              # __unicode__ on Python 2
        return self.username

 def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

 def has_module_perms(self, poll):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True 

# @property
# def is_staff(self):
#        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
#        return self.is_admin



