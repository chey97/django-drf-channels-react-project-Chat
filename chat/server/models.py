import uuid
from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from .validators import validate_icon_image_size, validate_image_file_extension


# Create your models here.


#hello chethiya

def server_icon_upload_path(instance, filename):
    return f"server/{instance.uuid}/server_icon/{filename}"


def server_banner_upload_path(instance, filename):
    return f"server/{instance.uuid}/server_banner/{filename}"


def category_icon_upload_path(instance, filename):
    return f"category/{instance.uuid}/category_icon/{filename}"


class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.FileField(upload_to=category_icon_upload_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.id:
            existing = Category.objects.filter(uuid=self.uuid).first()
            if existing and existing.icon != self.icon:
                existing.icon.delete(save=False)
        super(Category, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="server.Category")
    def category_delete_files(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon":
                instance.icon.delete(save=False)

    def __str__(self):
        return self.name


class Server(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="server_owner"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="server_category"
    )
    description = models.CharField(max_length=250, blank=True, null=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL)
    banner = models.ImageField(
        upload_to=server_banner_upload_path,
        blank=True,
        null=True,
        validators=[validate_image_file_extension],
    )
    icon = models.ImageField(
        upload_to=server_icon_upload_path,
        blank=True,
        null=True,
        validators=[validate_icon_image_size, validate_image_file_extension],
    )

    def save(self, *args, **kwargs):
        if self.id:
            existing = Server.objects.filter(uuid=self.uuid).first()
            if existing and existing.icon != self.icon:
                existing.icon.delete(save=False)
            if existing and existing.banner != self.banner:
                existing.banner.delete(save=False)
        super(Server, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="server.Server")
    def server_delete_files(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon" or field.name == "banner":
                instance.icon.delete(save=False)

    # def save(self, *args, **kwargs):
    #     self.name = self.name.lower()
    #     super(Server, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Channel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel_owner"
    )
    topic = models.CharField(max_length=250)
    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="channel_server"
    )

    def __str__(self):
        return self.name
