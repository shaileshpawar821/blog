from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login_view',views.login_view,name='login_view'),
    path('register_view',views.register_view,name='register_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('create_post',views.create_post,name='create_post'),
    path('edit_post/<int:pk>/',views.edit_post, name='edit_post') 
]