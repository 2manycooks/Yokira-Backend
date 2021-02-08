from yokira_app_gg.serializers import UserSerializer

def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'reqeust': request}).data
    }