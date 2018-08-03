from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'add_user$', views.add_user),
    url(r'add_board$', views.add_board),
    url(r'add_agree$', views.add_agree),
    url(r'add_comment$', views.add_comment),
]
