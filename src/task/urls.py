from django.urls import path

from . import views

urlpatterns = [
    path('' ,views.indexPage , name= "index_page" ),
    path('addTask/' , views.addTask , name="addTask_page"),
    path('updateTask/<str:pk>/' , views.updateTask , name="updateTask_page"),
    path('deleteTask/<str:pk>/' , views.deleteTask , name="deleteTask_page"),
] 