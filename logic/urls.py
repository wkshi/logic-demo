from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from logic import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^logic/$',
        views.LogicList.as_view(),
        name='logic-list'),
    url(r'^logic/(?P<pk>[0-9]+)/$',
        views.LogicDetail.as_view(),
        name='logic-detail'),
])
