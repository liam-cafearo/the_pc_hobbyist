from django.conf.urls import url
import views

urlpatterns = [
    url(r'^forum/$', views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', views.threads, name='threads')
    url(r'^new_thread/(?P<subject_id>\d+)/$', viewes.new_thread, name='new_thread')
]