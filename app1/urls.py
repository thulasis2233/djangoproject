from django.urls import path
from . import views
app_name='app1'
urlpatterns=[
    path('hello/',views.hello,name='hello'),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('logout/',views.logout,name='logout'),
    path('showimages/',views.showimages,name='showimages'),
    path('details/<int:id>',views.details,name='details'),
    path('mail/',views.mail,name='mail'),
]

