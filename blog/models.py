from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title

    def publish(self):
        self.post_date_posted = timezone.now()
        self.save()
        # todo: find out about this shit