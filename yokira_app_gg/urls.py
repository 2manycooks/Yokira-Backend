from django.conf.urls import url 
from yokira_app_gg import views 
 
urlpatterns = [ 
    url(r'^api/test$', views.test_list),
    url(r'^api/test/(?P<pk>[0-9]+)$', views.test_detail),
    url(r'^api/test/published$', views.test_list_published),
    url(r'^hello$', views.hello_world),
]