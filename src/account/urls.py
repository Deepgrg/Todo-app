from django.urls import path
from . import views


urlpatterns =[
    path('' , views.accountList , name='accountList_page'),
    path('register/' , views.register , name='register_page'),
    path('login/' , views.loginPage , name='login_page'),
    path('user/' , views.userAccount , name = 'userAccount_page'),
    
]