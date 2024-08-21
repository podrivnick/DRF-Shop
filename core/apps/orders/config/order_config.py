BASE_EXCEPTION_ORDERS = 'Something went wrong with order'


# Database order exceptions
INSUFFICIENT_QUANTITY = 'insufficient quantity of goods - {product_id}'
PRODUCT_NOT_FOUND_EXCEPTION = 'Product - {product_id} not found in database'
COULD_NOT_CREATE_ORDER_ITEM = "Could not create order items"

# Validation order exceptions noqa
## name receiver  noqa
TOO_MUCH_LENGTH_NAME_RECEIVER = "too much length name receiver"
NAME_RECEIVER_IS_EMPTY = "name receiver is empty"
NAME_RECEIVER_NOT_ALPHABETIC = "name receiver is not alphabetically"


## phone number  noqa
PHONE_NUMBER_CONTAINS_NOT_ONLY_DIGITS = "Phone number contains not only digits"
PHONE_NUMBER_CONTAINS_SOME_STRANGE_SYMBOLS = "Phone number contains some strange symbols"


# constants variable
MAX_LENGTH_PHONE_NUMBER = 20
MAX_LENGTH_NAME_RECEIVER = 60
