from django.core.validators import FileExtensionValidator
from django.db import models

from persik.validators import validate_image_model


class Video(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='videos/',
                            validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Persik\'s movie'  #for django admin panel
        ordering = ['create_at']


class Photo(models.Model):
    file = models.FileField(upload_to='photos/', validators=[validate_image_model])
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User\'s photos'  #for django admin panel
        ordering = ['create_at']


