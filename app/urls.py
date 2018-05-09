from django.conf.urls import url
from app import views
from django.conf import settings
from django.contrib.auth.views import logout

app_name='app'

urlpatterns = [
	url(r'^$', views.homepage,name="home"),
	url(r'^signup/$', views.signup, name="signup"),
	url(r'^login/$', views.user_login, name="login"),
	url(r'^logout/$', views.user_logout, name="logout"),
	url(r'^profile/$', views.profile, name="profile"),
]