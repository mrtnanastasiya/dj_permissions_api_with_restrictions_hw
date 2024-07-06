from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import AdvertisementOwnPermission
from advertisements.serializers import AdvertisementSerializer
from rest_framework.response import Response


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    # Валидация обновления/удаления чужого объявления
    # def update(self, request, *args, **kwargs):
    #     if self.get_object().creator != self.request.user:
    #         return Response(status=403, data={"message": "Пользователь не является владельцем"})
    #     return super().update(request, *args, **kwargs)
    #
    # def destroy(self, request, *args, **kwargs):
    #     if self.get_object().creator != self.request.user:
    #         return Response(status=403, data={"message": "Пользователь не является владельцем"})
    #     return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), AdvertisementOwnPermission()]
        elif self.action == "create":
            return [IsAuthenticated()]

        return [AllowAny()]
