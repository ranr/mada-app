from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index'),

    #nearby_events
    url(r'^nearby_events', 'home.views.nearby_events'),

    #new_event
    url(r'^new_event/([^/]+)/([^/]+)$', 'home.views.new_event'),

    #all_events
    url(r'^all_events$', 'home.views.all_events'),

    #get_rescuer
    url(r'^get_rescuer/([^/]+)$', 'home.views.get_rescuer'),  

    #all_rescuers
    url(r'^all_rescuers$', 'home.views.all_rescuers'),  
    # url(r'^mifmif/', include('mifmif.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    )
