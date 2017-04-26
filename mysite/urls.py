from django.conf.urls import include, url
from django.contrib import admin
# import blog
from django.contrib.auth.views import login, logout
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('blog.urls')),
    url(r'^$', views.post_list, name='index'),
    url(r'^accounts/profile', views.DocumentTypeListView.as_view(), name='index'),
    #url(r'^accounts/login/$',  login),
    url(r'^accounts/login',  login),
    url(r'^accounts/logout/$', views.logout),
    #url(r'^filling', views.fillingView, name='document'),
    url(r'^filling', views.fillingView),
    url(r'^accounts/registration', views.registrationView, name='registration'),
    url(r'^connect', views.RTFobject, name='test'),
    url(r'^userdata', views.userView, name='userView'),
    url(r'^contact', views.contact),
    url(r'^cabinet', views.cabinet),
    url(r'^worker/$', views.Worker, name='worker'),
    url(r'^worker/(?P<worker_id>\d+)/$', views.Worker, name='worker'),
    url(r'^worker_change', views.Worker_change, name='worker_change'),
    url(r'^filling_change', views.fillingView_change, name='document_change'),
    url(r'^orgdata', views.org_data, name='document_change'),
    url(r'^pass_set', views.pass_set, name='password_set'),
    url(r'^upload', views.upload_file, name='upload_file'),
    url(r'^download', views.download, name='download')
    #url(r'^media\/(<C:\\myproject\\Новая папка\\django 1.8\\mysite\\media\\uploads\\>'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
