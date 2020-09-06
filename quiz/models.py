from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ["created",]
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    label = models.CharField(max_length=500, blank=True, null=True)
    option1 = models.CharField(max_length=500,blank=True, null=True)
    option2 = models.CharField(max_length=500,blank=True, null=True)
    option3 = models.CharField(max_length=500,blank=True, null=True)
    option4 = models.CharField(max_length=500,blank=True, null=True)

    answer = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.label


class QuizUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.CharField(max_length=500, blank=True, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
