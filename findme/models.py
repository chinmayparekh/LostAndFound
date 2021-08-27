from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ItemLost(models.Model):
    ItemID = models.AutoField(primary_key=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    found = models.BooleanField(default=False)
    location = models.TextField(max_length=100)
    lost_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='findme/images', default="")
    found_location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
