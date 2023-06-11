from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def problem1(request):
    # Controller logic for problem1
    data = {
        'message': 'This is problem1.'
    }
    return Response(data)

@api_view(['GET'])
def problem2(request):
    # Controller logic for problem2
    data = {
        'message': 'This is problem2.'
    }
    return Response(data)

