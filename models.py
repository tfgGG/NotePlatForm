# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CaptchaCaptchastore(models.Model):
    challenge = models.CharField(max_length=32)
    response = models.CharField(max_length=32)
    hashkey = models.CharField(unique=True, max_length=40)
    expiration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captcha_captchastore'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    note_id = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'message'


class Note(models.Model):
    idnote = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    field = models.CharField(max_length=10)
    subjects = models.CharField(max_length=10)
    textbook = models.CharField(max_length=10)
    intro = models.CharField(max_length=45, blank=True, null=True)
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'note'


class NoteList(models.Model):
    idnote_list = models.AutoField(primary_key=True)
    list_text = models.CharField(max_length=45, blank=True, null=True)
    list_num = models.PositiveIntegerField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    noteid = models.ForeignKey(Note, models.DO_NOTHING, db_column='noteid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_list'


class Notebook(models.Model):
    id = models.IntegerField(primary_key=True)
    field = models.CharField(max_length=10)
    subjects = models.CharField(max_length=10)
    textbook = models.CharField(max_length=10)
    introduction = models.TextField()
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notebook'


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


class PollsDocument(models.Model):
    iddoc = models.IntegerField(primary_key=True)
    notelistid = models.ForeignKey(NoteList, models.DO_NOTHING, db_column='notelistid', blank=True, null=True)
    document = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_document'


class Profile(models.Model):
    idprofile = models.AutoField(db_column='idProfile', primary_key=True)  # Field name made lowercase.
    school = models.CharField(max_length=20, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    user_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'profile'
