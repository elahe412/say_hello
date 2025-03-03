from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@api_view(['GET'])
def say_hello(request):
    message = 'Hello World'
    return Response(message, status=HTTP_200_OK)


@api_view(['POST'])
def say_my_name(request):
    name = request.data.get('name', 'anonymous ')
    message = f'Hello {name}'
    return Response(message, status=HTTP_200_OK)


@api_view(['POST'])
def random_response(request):
    status_code=request.data.get('status',200)
    try:
        return Response(f"message with {status_code}",status=status_code)
    execpt: ValueError as e:
        return Response(str(e,status=500)
    
