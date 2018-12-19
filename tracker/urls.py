from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = ""

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/register/
    url(r'^accounts/register/$', views.register, name='register'),
    # ex: /polls/newrecipe/
    url(r'^logstats/$', views.logstats, name='logstats'),
    # ex: /polls/newrecipe/
    url(r'^trackstats/$', views.trackstats, name='trackstats'),
    # ex: /polls/newrecipe/
    url(r'^information/$', views.information, name='information'),
    # ex: /polls/newrecipe/
    url(r'^contact/$', views.contact, name='contact'),
    # ex: /polls/newrecipe/
    url(r'^discussion/$', views.discussion, name='discussion'),
    # ex: /polls/newrecipe/
    url(r'^health/$', views.health, name='health'),

    url(r'^publishannouncement/$', views.pubannouncement, name='pubannouncement'),

    url(r'^requests/$', views.requests, name='requests'),

    url(r'^quizzes/$', views.quizzes, name='quizzes'),

    # ex: /polls/submitrecipe/
    url(r'^newrecipe/$', views.submitrecipe, name='submitrecipe'),
    # ex: /polls/recipe/15/
    url(r'^stat/(?P<stat_id>[0-9]+)/$', views.stat, name='stat'),
    # ex: /polls/djcapizzi/
    url(r'^user/(?P<username>[a-zA-Z0-9]+)/$', views.userpage, name='userpage'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
