from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'http://127.0.0.1:8000/', include('blog.urls')),
]
