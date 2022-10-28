from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# user, like, like_count -> 좋아요 기능을 위해 넣어둔 모델
class Cashbook(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    content = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank = True)
    hashtags = models.ManyToManyField('Hashtag', blank = True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null = True)
    post_like = models.ManyToManyField(User,related_name='like_users', blank =True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    def __str__(self):
        return self.text

    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments', null=True)
    cashbook_id = models.ForeignKey(Cashbook, on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.CharField(max_length=50)

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
