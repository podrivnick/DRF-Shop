BASE_EXCEPTION_ORDERS = 'Something went wrong with order'


# Database order exceptions
INSUFFICIENT_QUANTITY = 'insufficient quantity of goods - {product_id}'
PRODUCT_NOT_FOUND_EXCEPTION = 'Product - {product_id} not found in database'
COULD_NOT_CREATE_ORDER_ITEM = "Could not create order items"

# Validation order exceptions noqa
TOO_MUCH_LENGTH_NAME_RECEIVER = "too much length name receiver"
NAME_RECEIVER_IS_EMPTY = "name receiver is empty"
NAME_RECEIVER_NOT_ALPHABETIC = "name receiver is not alphabetically"
