from django.db import models
from django.contrib.auth.models import User
# Create your models h


class Questions(models.Model):
    description=models.CharField(max_length=200)
    user=models.ForeignKey(User,models.CASCADE)
    image=models.ImageField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Answers(models.Model):
    question=models.ForeignKey(Questions,models.CASCADE)
    answer=models.CharField(max_length=200)
    user=models.ForeignKey(User,models.CASCADE)
    upvote=models.ManyToManyField(User)
    posted_date=models.DateTimeField(auto_now_add=True)



