from rest_framework import viewsets
from .models import Reward, RedemptionRequest
from .serializers import RewardSerializer, RedemptionRequestSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

class RedemptionRequestViewSet(viewsets.ModelViewSet):
    queryset = RedemptionRequest.objects.all()
    serializer_class = RedemptionRequestSerializer
