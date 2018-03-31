from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 30) #charfiled 는 항상 최대 길이 정해준다
    contents = models.TextField()
    view_count = models.IntegerField()

class Comment(models.Model):
    article = models.ForeignKey(Article)
    # ForeignKey란 무엇인가.
    comment = models.CharField(max_length = 100)
