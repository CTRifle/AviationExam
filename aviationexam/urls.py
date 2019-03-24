from django.contrib import admin
from django.conf.urls import url, include
from exam import views, urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.welcome,name="welcome"),
    url('exam/', include('exam.urls')),
    url('', include('users.urls')),
    url('admin/', admin.site.urls, name="admin"),
    url('login/', views.log_in, name="login"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
