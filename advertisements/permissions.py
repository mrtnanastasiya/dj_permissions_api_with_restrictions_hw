from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementOwnPermission(permissions.BasePermission):
    """
    Global permission check for advertisement own.
    """

    def has_permission(self, request, view):
        advertisement_id = view.kwargs.get('pk')
        return Advertisement.objects.filter(creator=request.user, id=advertisement_id).exists()
