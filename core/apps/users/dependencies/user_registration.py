from core.apps.common.utils.repository import ValidationRegisterData
from core.apps.users.service import UserRegistrationService


def registration_repository(serializer):
    return UserRegistrationService(ValidationRegisterData, serializer)
