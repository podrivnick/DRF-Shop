import pytest

from core.apps.orders.exceptions.validation_orders_exceptions import (
    DeliveryAddressNotAllowedSymbolsException,
    IncorrectDomainEmailException,
    IncorrectFormatEmailException,
    IsNameReceiverNotAlphabeticSpecException,
    PhoneNumberContainsNotAllowedSymblosException,
    PhoneNumberContainsNotOnlyDigitsException,
    SomeOrderDataIsEmptyException,
    TooMuchLengthNameReceiverException,
)
from core.apps.orders.services.validation_order import ValidationOrderDataService


class TestYourValidationService:
    @pytest.fixture
    def validation_service(self):
        return ValidationOrderDataService()

    def test_valid_data(self, validation_service):
        result = validation_service.validated_data_order(
            name_receiver="Артем Сырков",
            phone_number="+1-234-567-890",
            delivery_address="Some valid address",
            email="test@example.com",
        )
        expected_result = [
            "Артем Сырков",
            "+1-234-567-890",
            "Some valid address",
            "test@example.com",
        ]

        res = [item.as_generic_type() for item in result.values()]

        are_lists_equal = all(a == b for a, b in zip(res, expected_result))

        assert are_lists_equal

    def test_name_too_long(self, validation_service):
        with pytest.raises(TooMuchLengthNameReceiverException):
            validation_service.validated_data_order(
                name_receiver="Артем" * 100,  # name length exceeds the limit
                phone_number="+1-234-567-890",
                delivery_address="Some valid address",
                email="test@example.com",
            )

    def test_invalid_name_receiver(self, validation_service):
        with pytest.raises(IsNameReceiverNotAlphabeticSpecException):
            validation_service.validated_data_order(
                name_receiver="Артем123",
                phone_number="+1-234-567-890",
                delivery_address="Some valid address",
                email="test@example.com",
            )

    def test_invalid_phone_number_not_only_digits(self, validation_service):
        with pytest.raises(PhoneNumberContainsNotOnlyDigitsException):
            validation_service.validated_data_order(
                name_receiver="Артем Сырков",
                phone_number="12345abc890",
                delivery_address="Some valid address",
                email="test@example.com",
            )

    def test_invalid_phone_number_not_allowed_symbols(self, validation_service):
        with pytest.raises(PhoneNumberContainsNotAllowedSymblosException):
            validation_service.validated_data_order(
                name_receiver="Артем Сырков",
                phone_number="-123456-7890",
                delivery_address="Some valid address",
                email="fra3434@gmail.com",
            )

    def test_invalid_delivery_address(self, validation_service):
        with pytest.raises(DeliveryAddressNotAllowedSymbolsException):
            validation_service.validated_data_order(
                name_receiver="Артем Сырков",
                phone_number="+1-234-567-890",
                delivery_address="Some valid addre@@```~~ss",
                email="test@example.com",
            )

    def test_invalid_email_domain(self, validation_service):
        with pytest.raises(IncorrectDomainEmailException):
            validation_service.validated_data_order(
                name_receiver="Артем Сырков",
                phone_number="+1-234-567-890",
                delivery_address="Some valid address",
                email="test@domain..com",
            )

    def test_invalid_email_format(self, validation_service):
        with pytest.raises(IncorrectFormatEmailException):
            validation_service.validated_data_order(
                name_receiver="Артем Сырков",
                phone_number="+1-234-567-890",
                delivery_address="Some valid address",
                email="@domain.com",
            )

    # test for empty data
    def test_empty_name_receiver(self, validation_service):
        with pytest.raises(SomeOrderDataIsEmptyException):
            validation_service.validated_data_order(
                name_receiver="",
                phone_number="+1-234-567-890",
                delivery_address="Some valid address",
                email="@domain.com",
            )

    def test_empty_delivery_address(self, validation_service):
        with pytest.raises(SomeOrderDataIsEmptyException):
            validation_service.validated_data_order(
                name_receiver="Артем Сырков",
                phone_number="+1-234-567-890",
                delivery_address="",
                email="@domain.com",
            )

    def test_empty_email(self, validation_service):
        with pytest.raises(SomeOrderDataIsEmptyException):
            validation_service.validated_data_order(
                name_receiver="Артем Сырков",
                phone_number="+1-234-567-890",
                delivery_address="Some valid address",
                email="",
            )
