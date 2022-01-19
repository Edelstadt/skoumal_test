from django.db import models


class Author(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=255,
        blank=False,
    )
    email = models.EmailField(
        verbose_name="Email",
        blank=False,
    )
    phonenumber = models.CharField(
        verbose_name="Phone Number",
        max_length=255,
        blank=False,
    )


class WebSite(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=255,
        blank=False,
    )
    url = models.CharField(
        verbose_name="URL",
        max_length=255,
        blank=False,
    )
    author = models.ForeignKey(
        Author,
        verbose_name="Author",
        on_delete=models.CASCADE,
        null=False,
    )
    length = models.IntegerField(
        verbose_name="Length",
        null=False,
    )
