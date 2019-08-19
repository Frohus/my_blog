from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from tinymce import HTMLField
from lxml.html.clean import Cleaner

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = HTMLField('Content')
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def clean_body(self):
        cleaner = Cleaner(kill_tags=['pre', 'code', 'kbd', 'samp'])
        return cleaner.clean_html(self.post_content)