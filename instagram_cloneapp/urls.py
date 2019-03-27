from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url(r'^$',views.welcome, name='welcome'),
    url(r'^new/profile$', views.my_profile, name='myprofile'),
    url(r'^new/picture$', views.my_picture, name='mypicture'),
    url(r'^new/comment$', views.my_comment, name='mycomment'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
