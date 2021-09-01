from django.db import models
from django.contrib.auth.models import User
import cv2
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='register/images')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = cv2.imread(self.image.path, cv2.IMREAD_COLOR)
        down_width = 225
        down_height = 225
        down_points = (down_width, down_height)
        resized_down = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(self.image.path, resized_down)

    def __str__(self):
        return self.user.username
