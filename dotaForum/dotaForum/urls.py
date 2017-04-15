"""dotaForum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dota import views

urlpatterns = [
    url(r'^user/getall/$', views.getAllUser),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user),
    url(r'^user/insert/$', views.insertUser),
    url(r'^user/login/$', views.checkLogIn),

    url(r'^categories/getall/$', views.getAllCategories),
    url(r'^categories/(?P<category>[A-Za-z]+)/$', views.getCategory),

    url(r'^comment/getall/$', views.getAllComment),
    url(r'^comment/$', views.insertComment),
    url(r'^comment/(?P<id_comment>[0-9]+)/$', views.getCommentById),
    url(r'^comment/delete/(?P<id_comment>[0-9]+)/$', views.getAllComment),
    url(r'^comment/(?P<pk>[0-9]+)/$', views.updateComment),

    url(r'^likes/getall/$', views.getAllLikes),
    url(r'^likes/$', views.addLike),
    url(r'^likes/delete/(?P<id_post>[0-9]+)/(?P<id_user>[0-9]+)/$', views.deleteLike),
    url(r'^dislikes/getall/$', views.getAllDislikes),
    url(r'^dislikes/$', views.addDislike),

    url(r'^post/getall/(?P<judul>[A-Za-z]+)/$', views.getAllPost),
    url(r'^post/search/(?P<judul>[A-Za-z0-9]+)/$', views.getPostSearch),
    url(r'^/post/bycategory/(?P<category>[A-Za-z]+)/(?P<sort>[A-Za-z]+)/$', views.getPostByCategory),


    url(r'^message/getall/$', views.getAllMessage),
    url(r'^comment/$', views.insertMessage),
    # url(r'^comment/inbox/(?P<id_receiver>[0-9]+)/$', views.getInbox),
    # url(r'^comment/inbox/(?P<id_sender>[0-9]+)/(?P<id_receiver>[0-9]+)/$', views.getMsgFromId),
    url(r'^comment/delete/(?P<id_message>[0-9]+)/$', views.getAllMessage),
    url(r'^comment/(?P<pk>[0-9]+)/$', views.updateMessage),

    url(r'^reply/getall/$', views.getAllReply),

    url(r'^report/getall/$', views.getAllReport),

]

urlpatterns = format_suffix_patterns(urlpatterns)
