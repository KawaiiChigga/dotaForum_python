# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Categories(models.Model):
    id_category = models.AutoField(primary_key=True)
    category = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'categories'


class Comment(models.Model):
    id_comment = models.AutoField(primary_key=True)
    id_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='id_post')
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    isi_comment = models.TextField()
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment'


class Dislikes(models.Model):
    id_dislike = models.AutoField(primary_key=True)
    id_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='id_post')
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'dislikes'


class Likes(models.Model):
    id_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='id_post')
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    id_like = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'likes'


class Message(models.Model):
    id_message = models.AutoField(primary_key=True)
    id_sender = models.ForeignKey('User', models.DO_NOTHING, db_column='id_sender', related_name='sender')
    id_receiver = models.ForeignKey('User', models.DO_NOTHING, db_column='id_receiver', related_name='receiver')
    isi = models.TextField()
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'message'


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    judul = models.CharField(max_length=50)
    isi = models.TextField()
    date_time = models.DateTimeField()
    like_post = models.IntegerField()
    dislike_post = models.IntegerField()
    id_category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='id_category')

    class Meta:
        managed = False
        db_table = 'post'


class Reply(models.Model):
    id_reply = models.AutoField(primary_key=True)
    id_comment = models.ForeignKey(Comment, models.DO_NOTHING, db_column='id_comment')
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    isi = models.TextField()
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reply'


class Report(models.Model):
    id_report = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    id_post = models.ForeignKey(Post, models.DO_NOTHING, db_column='id_post')
    type_of_report = models.IntegerField()
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'report'


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=30)
    jenis_kelamin = models.CharField(max_length=3)
    url_foto = models.CharField(max_length=100)
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=30)
    level = models.IntegerField()
    date_time = models.DateTimeField()
    progress_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
