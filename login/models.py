from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    owner = models.CharField(max_length=20, blank=True, null=True)
    species = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    death = models.DateField(blank=True, null=True)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pet'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idprofile = models.PositiveIntegerField(db_column='idProfile', primary_key=True)  # Field name made lowercase.
    school = models.CharField(max_length=20, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='img')

    class Meta:
        managed = False
        db_table = 'profile'


    def create_profile(sender,**kwargs):
        if kwargs["created"]:
            user_profile = Profile.objects.create(user = kwargs['instance'])
        post_save.connect(create_profile,sender=User)

'''


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            print("printing a message...")

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
            instance.profile.save()

'''
