from django.conf.urls import include, url
from django.contrib import admin
# import blog
from django.contrib.auth.views import login
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.post_list, name='index'),
    url(r'^accounts/login',  login),
    url(r'^accounts/logout/$', views.logout),
    url(r'^filling', views.fillingView),
    url(r'^organization/(?P<pk>\d+)/$', views.OrganizationUpdate.as_view(), name='org_edit'),
    url(r'^accounts/registration', views.registrationView, name='registration'),
    url(r'^userdata', views.userview, name='userview'),
    url(r'^contact', views.contact),
    url(r'^cabinet', views.cabinet),
    url(r'^worker/$', views.worker, name='worker'),
    url(r'^worker/(?P<worker_id>\d+)/$', views.worker, name='worker'),
    url(r'^worker_update/(?P<pk>\d+)/$', views.WorkerUpdate.as_view(), name='worker_edit'),
    url(r'^orgdata', views.org_data, name='org_data'),
    url(r'^pass_set', views.pass_set, name='password_set'),
    url(r'^download', views.download, name='download'),
    url(r'^worker_data', views.choose_worker, name='worker_data'),
    url(r'^docx', views.download_docx, name='docx')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
