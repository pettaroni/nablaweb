from django.conf.urls import url
from .views import UnivDetailView, ExchangeListView, InfoDetailView


urlpatterns = [
    url(r'^info/(?P<pk>\d+)/$', InfoDetailView.as_view(), name="info_detail"),
    url(r'^(?P<pk>\d+)/$', UnivDetailView.as_view(), name="ex_detail_list"),
    url(r'^$', ExchangeListView.as_view(), name="ex_list"),
]