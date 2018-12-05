"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from oauth import views
from oauth.views import ApiEndpoint
import oauth2_provider.views as oauth2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('upload/', include('upload.urls')),
    path('person/', include('person.urls')),
    #path('oauth/', include('oauth.urls')),
    url(r'^api/hello/', ApiEndpoint.as_view()),
    url(r'^secret$', views.secret_page, name='secret'),
    #path('oauth/change/', views.change ),
    #path('oauth/', include(('oauth.urls','oauth2_provider'), namespace='oauth2_provider')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
   # url(r'^oauth/', include(('oauth.urls',"oauth2_provider"), namespace='oauth2_provider')),
    #url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

oauth2_endpoint_views = [
    url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
    url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    oauth2_endpoint_views += [
        url(r'^applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
        url(r'^applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        url(r'^applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        url(r'^applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        url(r'^applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]
    # OAuth2 Token Management endpoints
oauth2_endpoint_views += [
    url(r'^authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
    url(r'^authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(),
        name="authorized-token-delete"),
]
