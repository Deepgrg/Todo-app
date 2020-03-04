from django.urls import path
from . import views


urlpatterns =[
    path('' , views.accountList , name='accountList_page'),
]