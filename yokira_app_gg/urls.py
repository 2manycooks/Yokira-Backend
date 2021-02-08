from django.conf.urls import url, include
from django.urls import path, include
from yokira_app_gg import views
from .views import current_user, UserList


 
urlpatterns = [ 
    url(r'^api/test$', views.test_list),
    url(r'^api/test/(?P<pk>[0-9]+)$', views.test_detail),
    url(r'^api/test/published$', views.test_list_published),
    url(r'^hello$', views.hello_world),
    path('accounts/', include('django.contrib.auth.urls')),
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
]