from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    named_url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               blank=True, null=True, related_name='children')

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        elif self.url:
            return self.url
        else:
            return ''

    def __str__(self):
        return self.title
