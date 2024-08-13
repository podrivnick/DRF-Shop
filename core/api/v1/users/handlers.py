from rest_framework import (
    generics,
    status,
)
from rest_framework.response import Response

from core.apps.users.dependencies.user_registration import registration_repository
from core.apps.users.serializers import UserSerializer


class UserRegistrationAPI(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        if serializer:
            service = registration_repository(serializer)
        else:
            return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        service.validate()

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
