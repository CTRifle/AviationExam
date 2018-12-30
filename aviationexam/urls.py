from django.contrib import admin
from django.conf.urls import url, include
from exam import views, urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.welcome,name="welcome"),
    url('exam/', include('exam.urls')),
    url('admin/', admin.site.urls, name="admin"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
