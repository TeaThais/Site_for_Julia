from django.db import models
from django.urls import reverse


class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


class MainPage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos', default=None, null=True, blank=True, verbose_name='Image')
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'


class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos', default=None, null=True, blank=True, verbose_name='Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


class Status(models.IntegerChoices):
    DRAFT = 0, 'Черновик'
    PUBLISHED = 1, 'Опубликовано'


class Polytheism(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='photos', default=None, null=True, blank=True, verbose_name='Image')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLISHED)
    offer = models.ForeignKey('Offer', on_delete=models.PROTECT, null=True)

    objects = models.Manager()
    published = PublishedModel()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Неоязычество'
        verbose_name_plural = 'Неоязычество'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    def get_absolute_url(self):
        return reverse('polytheism_posts', kwargs={'post_slug': self.slug})


class Magic(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='photos', default=None, null=True, blank=True, verbose_name='Image')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLISHED)
    offer = models.ForeignKey('Offer', on_delete=models.PROTECT, null=True)

    objects = models.Manager()
    published = PublishedModel()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магия'
        verbose_name_plural = 'Магия'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    def get_absolute_url(self):
        return reverse('magic_posts', kwargs={'post_slug': self.slug})


class Tarot(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='photos', default=None, null=True, blank=True, verbose_name='Image')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLISHED)
    offer = models.ForeignKey('Offer', on_delete=models.PROTECT, null=True)

    objects = models.Manager()
    published = PublishedModel()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Таро'
        verbose_name_plural = 'Таро'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    def get_absolute_url(self):
        return reverse('tarot_posts', kwargs={'post_slug': self.slug})