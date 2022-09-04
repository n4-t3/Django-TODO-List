from django.urls import path
from . import views

app_name="Todos_App"

urlpatterns = [
    path('<int:pk>', views.list_page,name="list_page"),
]
