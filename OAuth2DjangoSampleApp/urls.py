
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='sampleAppOAuth2:index')),
    url(r'^(?i)sampleAppOAuth2/', include('sampleAppOAuth2.urls', namespace='sampleAppOAuth2')),
    url(r'^(?i)admin/', admin.site.urls),
]
