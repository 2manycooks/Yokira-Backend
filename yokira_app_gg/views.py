from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status, viewsets, permissions
from django.contrib.auth.models import User, Group
from yokira_app_gg.models import Test
from yokira_app_gg.serializers import UserSerializer, GroupSerializer, TestSerializer




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return JsonResponse({"message": "Got some data!", "data": request.data})
    return JsonResponse({"message": "Hello, world!"})

@api_view(['GET', 'POST', 'DELETE'])
def test_list(request):
    if request.method == 'GET':
        tests = Test.objects.all()
        title = request.GET.get('title')
        if not title:
            title = ""
        test = tests.filter(title__icontains=title)
        test_serializer = TestSerializer(test, many=True)
        return JsonResponse(test_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    """ elif request.method == 'POST':
        test_data = JSONParser().parse(request)
        test_serializer = TestSerializer(data=test_data)
        if test_serializer.is_valid():
            test_serializer.save()
            return JsonResponse(test_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(test_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(json.dumps({'key': 'value'},default=json_util.default))

    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT) """
 
@api_view(['GET', 'PUT', 'DELETE'])
def test_detail(request, pk):
    # ... tutorial = Tutorial.objects.get(pk=pk)
 
    if request.method == 'GET': 
        tutorial_serializer = TestSerializer(test) 
        return JsonResponse(test_serializer.data)

    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
     # find tutorial by pk (id)
    try: 
        test = Test.objects.get(pk=pk) 
    except Test.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

        
@api_view(['GET'])
def test_list_published(request):
    # GET all published tutorials
    tutorials = Tutorial.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    try:
        test = Test.objects.get()
    except Test.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 