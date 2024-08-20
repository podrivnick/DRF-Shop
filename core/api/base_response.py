from rest_framework import status
from rest_framework.response import Response


class StandartResponseAPI:
    def create_response(self, data=None, status_code=status.HTTP_200_OK, message=None):
        response_data = {
            'status': 'success' if status_code in range(200, 300) else 'error',
            'data': data,
            'message': message,
        }

        return Response(response_data, status=status_code)
