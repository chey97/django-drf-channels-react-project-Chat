from PIL import Image
from django.core.exceptions import ValidationError
import os


def validate_icon_image_size(image):
    if image:
        with Image.open(image) as img:
            if img.width > 70 or img.height > 70:
                raise ValidationError(f"Image size should be less than 70x70 - size of the image you uploaded: {img.size}")
    
    
def validate_image_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpg', '.jpeg', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')