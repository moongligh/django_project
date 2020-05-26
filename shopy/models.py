from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# 커뮤니티 모델
class Community(models.Model):
    subject = models.CharField(max_length=200)
    category_local = models.CharField(max_length=30)
    category_sectors = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, related_name='voter_community')

    def __str__(self):
        return self.subject

# Q&A 모델
class QNA(models.Model):
    subject = models.CharField(max_length=200)
    category_local = models.CharField(max_length=30)
    category_sectors = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, related_name='voter_QNA')

    def __str__(self):
        return self.subject

# 팁과 노하우 모델
class TipNknowhow(models.Model):
    subject = models.CharField(max_length=200)
    category_local = models.CharField(max_length=30)
    category_sectors = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, related_name='voter_tipNknowhow')

    def __str__(self):
        return self.subject

# 댓글 모델
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    community = models.ForeignKey(Community, on_delete= models.CASCADE, null=True, blank=True)
    QNA = models.ForeignKey(QNA, on_delete= models.CASCADE, null=True, blank=True)
    tipNknowhow = models.ForeignKey(TipNknowhow, on_delete= models.CASCADE, null=True, blank=True)