import os
from django.core.exceptions import ValidationError


def validate_image_model(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpeg', '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_image_form(img):
    size = img.size
    format = img.name.split(".")[-1]
    avaible_formats = [
        'png',
        'jpeg',
        'jpg',
    ]
    if size > 4194304:
        return None
    if format not in avaible_formats:
        return None
    return img