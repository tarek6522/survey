from django.db import models
from django.contrib.auth.models import User
# MinValueValidator مستورد ولكن لم يُستخدم، احذفه إن لم تكن بحاجة إليه
from django.core.validators import MinValueValidator

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    target_group = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    response = models.TextField()
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user_display = self.user.username if self.user else "Anonymous"
        return f"{user_display} - {self.question.text}"
