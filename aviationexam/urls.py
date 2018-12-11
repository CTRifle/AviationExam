from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from exam import views, urls

urlpatterns = [
    url(r'^$',views.welcome,name="welcome"),
    url('exam/', include('exam.urls')),
    url('admin/', admin.site.urls, name="admin"),
]
