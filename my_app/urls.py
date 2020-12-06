from django.conf.urls import url
from . import views


app_name = 'my_app'


urlpatterns = [

    url('login/', views.login_page, name='login_page'),
    url('signup/', views.signup, name='signup'),
    url('logout/', views.logoutuser, name='logoutuser'),
    url('create/', views.createtodo, name='createtodo'),
    url('completed/', views.completed, name="completed"),



]
