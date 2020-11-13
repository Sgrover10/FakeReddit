from django.db import models
from Login_Reg_App.models import User

class PostManager(models.Manager):
    def empty_validator(self, postdata):
        errors=""
        if len(postdata['subject']) < 1:
            errors="Your subject cannot be empty."
        if len(postdata['content']) < 3:
            errors="Your post must be at least 3 characters"
        return errors

class Post(models.Model):
    subject=models.CharField(max_length=255)
    content=models.TextField()
    poster=models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    likes=models.ManyToManyField(User, related_name="likes")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=PostManager()

class Comment(models.Model):
    content=models.TextField()
    poster=models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post=models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    # likes=models.ManyToManyField(User, related_name="likes")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# Create your models here.
