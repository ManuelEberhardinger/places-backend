from django.conf.urls import url
from first import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^places/(?P<label>\w{0,50})$', views.get_locations),
    url(r'^labels$', views.get_all_labels),
    url(r'^image$', views.UserUploadedPicture.as_view()),
    url(r'^image/(?P<id>\w{0,50})$', views.get_picture_from_id)
]