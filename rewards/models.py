from django.db import models
from django.contrib.auth.models import User
from django..validators import MinValueValidator

class Reward(models.Model):
    name = models.CharField(max_length=100)
    points_required = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class RedemptionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.reward.name}"


