from django.conf.urls import url
from . import views
app_name='polls'
urlpatterns=[
	url('',views.index,name='index')
]