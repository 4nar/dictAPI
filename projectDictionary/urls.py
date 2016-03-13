"""projectDictionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from dictionary.views import WordViewSet, WordDetail, LangView, LangDetailed
from dictionary.models import Word
from dictionary.serializers import WordSerializer
from rest_framework.generics import ListAPIView

# router = routers.DefaultRouter()
# router.register(r'words', ListAPIView.as_view(queryset=Word.objects.all(), serializer_class=WordSerializer), base_name='words_list')
# router.register(r'words/(?P<title>.+)/$',views.WordViewSet.as_view(), base_name='words_by_lang')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/words/$', WordViewSet.as_view()),
    url(r'^api/words/$', WordViewSet.as_view()),
    # url(r'^api/words/(?P<pk>[0-9]+)/$', WordDetail.as_view()),
    url(r'^api/words/(?P<language>.+)/(?P<pk>[0-9]+)/$', LangDetailed.as_view()),
    url(r'^api/words/(?P<language>.+)/(?P<pk>[0-9]+)/\?translate=(?P<t_language>.+)/$', LangDetailed.as_view()),
    url(r'^api/words/(?P<language>.+)/$', LangView.as_view()),
    url(r'^api/words/(?P<language>.+)/\?title__istartswith=(?P<symbol>)/$', LangView.as_view()),
    
    # url(r'^api/', include(router.urls, namespace='api')),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
