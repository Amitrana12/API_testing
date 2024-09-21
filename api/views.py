import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def registration(request):
    responser = [{
        'responseCode' : 1,
        'errorCode': "00",
        'description':'Merchant Registered successfully'
    },
    {
        'responseCode' : 1,
        'errorCode': "2",
        'description':'Registration is already completed, Please perform Authentication.'
    },
    {
        'responseCode' : 0,
        'errorCode': 'XX',
        'description':'Retry or Failed.'
    }]
    registered = random.choice(responser)
    
    if registered['responseCode'] == 0:
        return Response(registered, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(registered, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def authentication(request):
    responser = [{
        'responseCode' : 1,
        'errorCode': "0",
        'description':'Merchant Authenticate Successfully.'
    },
    {
        'responseCode' : 0,
        'errorCode': 'XX',
        'description':'Error from bank.'
    },
    {
        'responseCode' : 3,
        'errorCode': 'NA',
        'description':'Invalid Request, Please try again.'
    }]
    authenticated = random.choice(responser)
    
    if authenticated['responseCode'] == 3:
        return Response(authenticated, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(authenticated, status=status.HTTP_200_OK)

@api_view(['POST'])   
def authcashwithdraw(request):
    responser = [{
        'responseCode' : 1,
        'description':'SUCCESS (Provided Message)'
    },
    {
        'responseCode' : 0,
        'description':'FAILED (Provided Message) ( HIT Threeway API)'
    },
    {
        'responseCode' : 2,
        'description':'ERROR OR REQUEST TIMEOUT( HIT QUERY API)'
    }]
    authenticated = random.choice(responser)
    
    Response(authenticated, status=status.HTTP_200_OK)