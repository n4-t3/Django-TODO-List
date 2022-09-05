from django.urls import path
from . import views

app_name = 'Authentication_App'

urlpatterns = [
    path('', views.index, name='home_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('error/', views.error_page, name='error_page'),
    path('profile/<int:pk>', views.profile_page, name='profile_page'),
    path('delete/<int:pk>', views.delete_user, name='delete_user'),
]
