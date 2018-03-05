from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.buckets),
    url(r'^(\d+)/$', views.bucketDetails)
]

