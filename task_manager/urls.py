"""from django.contrib import admin
from django.urls import path
from task_manager import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('registration/', views.registration_page, name='registration_page'),
    path('login/', views.login_page, name='login_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<int:pk>/', views.create_task, name='create_task'),
    path('dashboard/<int:pk>/', views.update_task, name='update_task'),
    path('dashboard/<int:pk>/', views.delete_task, name='delete_task'),
    # Corrected view name here
    path('logout/', views.logout_user, name='logout_user'),
]
"""
from django.contrib import admin
from django.urls import path
from task_manager import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home_page, name='base'),
    path('registration/', views.registration_page, name='registration_page'),
    path('login/', views.login_page, name='login_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('check', views.check, name='check'),
    path('dashboard/update/<int:pk>/',
         views.update_task, name='update_task'),
    path('dashboard/delete/<int:pk>/',
         views.delete_task, name='delete_task'),
    path('logout/', views.logout_user, name='logout_user'),
]
