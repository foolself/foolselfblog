from django.conf.urls import url
from blog import views

urlpatterns = [url(r'^$', views.home),
               url(r'^about/',views.about),
               url(r'^article/(?P<pk>[0-9]+)/$',views.article_detail),
               url(r'^drafts/$',views.article_draft_list,name='article_draft_list'),
               url(r'^article/(?P<pk>[0-9]+)/edit/$',views.article_edit,name='article_edit'),
               url(r'^article/(?P<pk>[0-9]+)/publish/$',views.article_publish,name='article_publish'),
               url(r'^article/(?P<pk>[0-9]+)/remove/$',views.article_remove,name='article_remove'),
               ]