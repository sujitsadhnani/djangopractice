from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [    
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('medposting', views.medposting, name='medposting'),
    path('login', views.login, name='login'),
    path('forgot_pass', views.forgot_pass, name='forgot_pass'),
    path('reset_pass', views.reset_pass, name='reset_pass'),
    path('logout', views.logout, name='logout'),
    path('like', views.like, name='like'),
    path('best_docs', views.best_docs, name='best_docs'),
    # path('', views., name=''),
]
