from django.conf.urls import url, include
from . import views, auth_views
from django.urls import path

urlpatterns = [
    url(r'add_user$', views.add_user),
    url(r'add_board$', views.add_board),
    url(r'add_agree$', views.add_agree),
    url(r'add_comment$', views.add_comment),
    url(r'get_UID$', views.get_UID),
    url(r'get_board$', views.get_board),
    url(r'get_agreeNumber$', views.get_agreeNumber),
    url(r'get_disagreeNumber$', views.get_disagreeNumber),
    url(r'get_amAgree$', views.get_amAgree),
    url(r'get_username$', views.get_username),
    url(r'get_comments$', views.get_comments),
    url(r'get_totalNumber$', views.get_totalNumber),
    
    path('login', auth_views.login, name='login'),
    path('authenticate', auth_views.authenticate, name='authenticate'),
    path('logout', auth_views.login, name='logout')
]
