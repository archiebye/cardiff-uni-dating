from django.conf.urls import url
from . import views
#from mysite.core import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.signup, name='signup'),
	url(r'^update_profile/$', views.update_profile, name='update_profile'),
	#url(r'^signin/$', views.signin, name='signin'),
	url(r'^signin/$', auth_views.login, {'template_name': 'signin/signin.html'}, name='login'),
	url(r'^users/$', views.userlist, name='users'),
	url(r'^signout/$', views.signout, name='signout'),
]