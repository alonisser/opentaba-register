from django.conf.urls import patterns, include, url
from django.db.models import get_app, get_models

from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin

def autoregister(*app_list):
    for app_name in app_list:
        app_models = get_app(app_name)
        for model in get_models(app_models):
            try:
                admin.site.register(model)
            except AlreadyRegistered:
                pass


autoregister()


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'register.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^feeds/', include('planet.urls'))
)
