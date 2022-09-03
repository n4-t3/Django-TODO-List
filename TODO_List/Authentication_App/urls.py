from django.urls import path
from . import views

app_name = 'Authentication_App'

urlpatterns = [
    path('', views.index,name='home_page')
]