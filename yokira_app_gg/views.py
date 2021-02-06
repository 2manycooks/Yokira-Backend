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


@api_view(['GET', 'POST', 'DELETE'])
def test_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            test = test.filter(title__icontains=title)
        
        test_serializer = TestSerializer(test, many=True)
        return JsonResponse(test_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        test_data = JSONParser().parse(request)
        test_serializer = TutorialSerializer(data=tutorial_data)
        if test_serializer.is_valid():
            test_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET', 'PUT', 'DELETE'])
def test_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        test = Test.objects.get(pk=pk) 
    except Test.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def test_list_published(request):
    # GET all published tutorials
    try:
        test = Test.objects.get()
    except Test.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 