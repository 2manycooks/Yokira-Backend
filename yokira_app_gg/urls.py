from django.conf.urls import url 
from yokira_app_gg import views 
 
urlpatterns = [ 
    url(r'^api/yokira_app_gg$', views.test_list),
    url(r'^api/yokira_app_gg/(?P<pk>[0-9]+)$', views.test_detail),
    url(r'^api/yokira_app_gg/published$', views.test_list_published)
]