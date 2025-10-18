from django.db import models

from users.models import User
# Create your models here.
class BasicPost(models.Model):
    title = models.CharField("제목",max_length=100)
    content = models.TextField("내용")
    created = models.DateTimeField("생성일", auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class CommentPost(models.Model):
    comment = models.TextField("댓글내용")
    created = models.DateTimeField("생성일", auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment