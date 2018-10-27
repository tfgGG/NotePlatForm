from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    idnote = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)     #更改文字長度
    field = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100)
    textbook = models.CharField(max_length=100)
    intro = models.CharField(max_length=100, blank=True, null=True)
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'note'


class NoteList(models.Model):
    idnote_list = models.AutoField(primary_key=True)
    list_text = models.CharField(max_length=45, blank=True, null=True)
    list_num = models.PositiveIntegerField(blank=True, null=True)
    note = models.CharField(max_length=3000, blank=True, null=True)
    noteid = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_list'

class PollsDocument(models.Model):
    iddoc = models.IntegerField(primary_key=True)
    notelistid = models.ForeignKey(NoteList, models.DO_NOTHING, db_column='notelistid', blank=True, null=True)
    document = models.FileField(max_length=100)
    uploaded_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_document'


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    note_id = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'message'

class UploadMessage2(models.Model):
    id = models.IntegerField(primary_key=True)
    note_id = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=100)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_message2'

class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    idnote = models.ForeignKey(Note, models.DO_NOTHING, db_column='idnote', blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'upload_favorite'
