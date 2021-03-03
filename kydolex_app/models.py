from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Kydolex_Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    title_sub = models.CharField("タイトル", max_length=200)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title


class Kydolex_Post2(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    sub = models.CharField("タイトル", max_length=200, null=True,)

    sub_midle = models.CharField("中間", max_length=200, null=True,)
    sub_midle2 = models.CharField("中間2", max_length=200, null=True,)
    sub_midle3 = models.CharField("中間3", max_length=200, null=True,)

    content = models.TextField("本文")
    sub_content = models.TextField("中間本文", max_length=200, null=True,)
    sub_content2 = models.TextField("中間本文2", max_length=200, null=True,)
    sub_content3 = models.TextField("中間本文3", max_length=200, null=True,)

    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    sub_image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    sub_image2 = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    sub_image3 = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title


class Kydolex_Post3(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    title_name = models.CharField("name", max_length=200, null=True,)
    title_id = models.CharField("id", max_length=200, null=True,)
    title_url = models.CharField("url", max_length=200, null=True,)
    content = models.TextField("本文")
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title


class Kydolex_Post4(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title


class Kydolex_Post5(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title


class Kydolex_list_WebDesign(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("説明", max_length=200, null=True,)
    content_url = models.TextField("URL", max_length=200, null=True,)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title

class Kydolex_list_UIUX(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("説明", max_length=200, null=True,)
    content_url = models.TextField("URL", max_length=200, null=True,)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title

class Kydolex_list_Icon(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("説明", max_length=200, null=True,)
    content_url = models.TextField("URL", max_length=200, null=True,)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title

class Kydolex_list_3D(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("説明", max_length=200, null=True,)
    content_url = models.TextField("URL", max_length=200, null=True,)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title

class Kydolex_list_graphic(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("説明", max_length=200, null=True,)
    content_url = models.TextField("URL", max_length=200, null=True,)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title

class Kydolex_list_video(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("説明", max_length=200, null=True,)
    content_url = models.TextField("URL", max_length=200, null=True,)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title

class Kydolex_list_Photograth(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("説明", max_length=200, null=True,)
    content_url = models.TextField("URL", max_length=200, null=True,)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title

class Kydolex_list_Image(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("説明", max_length=200, null=True,)
    content_url = models.TextField("URL", max_length=200, null=True,)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title

class Kydolex_list_Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("説明", max_length=200, null=True,)
    content_url = models.TextField("URL", max_length=200, null=True,)
    image = models.ImageField(
        upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title

