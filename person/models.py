from django.db import models
from django.contrib.auth.models import User
from upload.models import Note
from oauth2_provider.models import AbstractApplication
# Create your models here.
class User(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.ImageField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class Group(models.Model):
    idgroup = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45,blank=True,null=True)
    creator = models.ForeignKey(User, models.DO_NOTHING, db_column='creator', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group'

class Groupuser(models.Model):
    idgroup = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userid', blank=True, null=True)
    group = models.ForeignKey(Group, models.DO_NOTHING, db_column='group', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groupuser'

class Plan(models.Model):
    idplan = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45,blank=True,null=True)
    groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='groupid',blank=True,null=True)

    class Meta:
        managed = False
        db_table = 'plan'

class Plandetail(models.Model):
    idplandetail = models.AutoField(primary_key=True)
    note = models.ForeignKey(Note, models.DO_NOTHING, db_column='note',blank=True,null=True)
    assign = models.ForeignKey(User, models.DO_NOTHING, db_column='assign',blank=True,null=True)
    start = models.CharField(max_length=50,blank=True,null=True)
    end = models.CharField(max_length=50,blank=True,null=True)
    plan = models.ForeignKey(Plan,models.DO_NOTHING,db_column='plan',blank=True,null=True)

    class Meta:
        managed = False
        db_table = 'plandetail'

class Chat(models.Model):
    idchat = models.AutoField(primary_key=True)
    time = models.CharField(max_length=45, blank=True, null=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userid', blank=True, null=True)
    teamid = models.ForeignKey(Group, models.DO_NOTHING, db_column='teamid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat'

class MyApplication(AbstractApplication):
    logo = models.ImageField()
    agree = models.BooleanField()

class Groupnote(models.Model):
    idgroupnote = models.AutoField(primary_key=True)
    note = models.ForeignKey(Note, models.DO_NOTHING, db_column='note',blank=True,null=True)
    group = models.ForeignKey(Group, models.DO_NOTHING, db_column='group', blank=True, null=True)
