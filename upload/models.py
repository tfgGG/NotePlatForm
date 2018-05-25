from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    idnote = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
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
    noteid = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_list'
