from rest_framework.decorators import api_view
from rest_framework.response import Response
from problems.solution.Solution2 import Solution2
from rest_framework import status
from problems.solution.Solution1 import  queensAttack
@api_view(['POST'])
def problem1(request):
    # Controller logic for problem1
    try: 
          rq=int(request.data.get('rq'))-1
          data = {
            'response': queensAttack(int(request.data.get('n')),int(request.data.get('k')),rq,int(request.data.get('cq'))-1,request.data.get('obstacles')),
             'ok':True
          }
          return Response(data)
    except ValueError as e:    
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)      
   

@api_view(['POST'])
def problem2(request):
    # Controller logic for problem2
    try:
            solution=Solution2(request.data.get('input'))
            data = {
                'response': solution.calculate_max_value(),
                 'ok':True,
            }
            return Response(data, status=status.HTTP_200_OK)
    except ValueError as e:    
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

