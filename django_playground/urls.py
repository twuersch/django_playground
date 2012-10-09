from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r"^iterate_many_to_many/", "sandbox.views.iterate_many_to_many"),
    url(r"^is_many_to_many_save_required/", "sandbox.views.is_many_to_many_save_required"),
)
