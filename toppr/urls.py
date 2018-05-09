"""toppr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/', include('app.urls')),
    url(r'^User_list/',views.Users_List.as_view()),
    url(r'^UserProfile_list/',views.UserProfile_List.as_view()),
    url(r'^Topic_list/',views.Topic_List.as_view()),
    url(r'^Subtopic_list/',views.Subtopic_List.as_view()),
    url(r'^Question_list/',views.Question_List.as_view()),
    url(r'^Answer_list/',views.Answer_List.as_view()),
    url(r'^Attempt_list/',views.Quiz_Question_List.as_view()),
    url(r'^Quiz_list/',views.Quiz_List.as_view()),
    url(r'^Quiz_Question_list/',views.Quiz_Question_List.as_view()),
]
