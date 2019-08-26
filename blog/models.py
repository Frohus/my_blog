from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from tinymce import HTMLField
from lxml.html.clean import Cleaner


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField('Content')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def clean_body(self):
        cleaner = Cleaner(kill_tags=['pre', 'code', 'kbd', 'samp'])
        return cleaner.clean_html(self.content)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
