from django.db import models
from gag.mixins import TranslateMixin
from gag.helpers import UploadTo
import os


class Category(TranslateMixin, models.Model):
    translate_fields = ['name']
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    image = models.ImageField(upload_to=UploadTo("category"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Katigoriya'
        verbose_name_plural = 'Katigoriyalar'

class Post(models.Model):
    user = models.ForeignKey("client.User", on_delete=models.RESTRICT)
    category = models.ForeignKey('Category', on_delete=models.RESTRICT)
    comment = models.TextField()
    file = models.FileField(verbose_name="Rasim/Video", upload_to=UploadTo("post"))
    like = models.SmallIntegerField(default=0)
    dislike = models.SmallIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    @property
    def ext(self):
        return (os.path.splitext(self.file.name)[1])[1:].lower()


    @property
    def is_image(self):
        return self.ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']


    @property
    def is_video(self):
        return self.ext in ['mp4', 'mpeg']


    @property
    def is_audio(self):
        return self.ext in ['mp3', 'wav']


class PostComment(models.Model):
    parent = models.ForeignKey('PostComment', on_delete=models.RESTRICT, null=True, default=True)
    post = models.ForeignKey('Post', on_delete=models.RESTRICT)
    user = models.ForeignKey('client.User', on_delete=models.RESTRICT)
    comment = models.TextField()
    image = models.ImageField(upload_to=UploadTo('Comment'))
    like = models.SmallIntegerField(default=0)
    dislike = models.SmallIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)


