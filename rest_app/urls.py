from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
		url(r'^blogs/$',views.BlogList.as_view()),
		url(r'^blogs/(?P<pk>[0-9]+)$',views.BlogDetail.as_view()),
		url(r'^users/$',views.UserList.as_view()),
		url(r'^users/(?P<pk>[0-9]+)$',views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
