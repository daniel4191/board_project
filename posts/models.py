from django.db import models

from users.models import User
# Create your models here.
class Post(models.Model):    
    title = models.CharField("제목", max_length=100, blank=False)
    content = models.TextField("내용")
    tags = models.CharField("태그", max_length=100, blank=True)
    created = models.DateTimeField("생성일시", auto_now_add=True)
    updated = models.DateTimeField("수정일", auto_now=True)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
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