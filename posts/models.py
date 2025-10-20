from django.db import models

from users.models import User
# Create your models here.
"""
내가 작성한 post 클래스
class BasicPost(models.Model):
    title = models.CharField("제목",max_length=100)
    content = models.TextField("내용")
    created = models.DateTimeField("생성일", auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
"""

    
class CommentPost(models.Model):
    comment = models.TextField("댓글내용")
    created = models.DateTimeField("생성일", auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    
    
class Post(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE
    )
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)
    
class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="포스트",
        on_delete=models.CASCADE
    )
    photo = models.ImageField("사진", upload_to="post")
    
class Comment(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, verbose_name="포스트", on_delete=models.CASCADE)
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)