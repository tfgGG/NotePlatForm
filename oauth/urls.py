from django.conf.urls import url, include
import oauth2_provider.views as oauth2_views
from django.conf import settings
from .views import ApiEndpoint
from .import views

# OAuth2 provider endpoints

#if settings.DEBUG:
    # OAuth2 Application Management endpoints


urlpatterns = [
    # OAuth 2 endpoints:
    
    url(r'^api/hello', ApiEndpoint.as_view()),
  # an example resource endpoint
     #url(r'^secret$', 'my.views.secret_page', name='secret'),
]