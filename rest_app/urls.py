from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [	
        url(r'^$', views.api_root),
		url(r'^blogs/$',views.BlogList.as_view(),name='blogs-list'),
		url(r'^blogs/(?P<pk>[0-9]+)$',views.BlogDetail.as_view(),name='blog-detail'),
		url(r'^users/$',views.UserList.as_view(),name='users-list'),
		url(r'^users/(?P<pk>[0-9]+)$',views.UserDetail.as_view(),name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
