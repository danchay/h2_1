# """h2_1 URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.8/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Add an import:  from blog import urls as blog_urls
#     2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
# """
# from django.conf.urls import include, url
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
# ]


from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.admin import AdminSite
AdminSite.site_header = 'Hacking To 100: '
AdminSite.site_title = 'Hacking To 100'
AdminSite.index_title = 'H2100 Apps Admin'


from .settings import MEDIA_URL
from .settings import STATIC_URL, STATIC_ROOT
from .views import * 
from blog import views as blog_views

 




urlpatterns = [
    url(r'^about-this-site/$', about, name='about'),
    url(r'^$', blog_views.index, name="index"),
    url(r'^index/', blog_views.index),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^backend/', include(admin.site.urls)),
    url(r'^ckwotes/', include('ckwotes.urls', namespace='ckwotes')),
    # url(r'^about/', views.about, name="about"),

] 


if settings.DEBUG:
    from .settings import MEDIA_ROOT
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

handler400 = 'h2_1.views.bad_request'
handler403 = 'h2_1.views.permission_denied'
handler404 = 'h2_1.views.page_not_found'
handler500 = 'h2_1.views.server_error'