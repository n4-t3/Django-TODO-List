from django.urls import path
from . import views

app_name = "Todos_App"

urlpatterns = [
    path('<int:pk>/<int:id>', views.list_page, name="list_page"),
    path('delete/<int:id>', views.delete_task, name="delete_task"),
    path('edit/<int:id>', views.edit_task, name='edit_task')
]
