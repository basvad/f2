from p_pols.views import index, poll, detail, results, vote, CustomLoginView,stat
from django.urls import path  
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import re_path
from django.conf.urls import include


app_name = 'common'  
urlpatterns = [  
    re_path(r'stat', stat, name='stat'),
    re_path(r'poll', poll, name='poll'),  
    path('', index, name='index'),  
    #path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    re_path(r'^(?P<poll_id>\d+)/$', detail, name='detail'),
    # ex: /polls/5/results/
    re_path(r'^(?P<poll_id>\d+)/results/$', results, name='results'),
    # ex: /polls/5/vote/
    re_path(r'^(?P<poll_id>\d+)/vote/$', vote, name='vote'),
]