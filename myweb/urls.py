from django.urls import path,include
from django.contrib.auth import views as aunt_views
from . import views
from . import *

urlpatterns = [ 
   path('index', views.index, name='index'),
   path('', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
   path('signup', views.sign_up, name='signup'), 
   path('logout',views.logout, name='logout'),
   path('contract',views.contract, name='contract'),
   path('addvegetable',views.addvegetable, name='addvegetable'),
   path('allvegetable',views.showVegetable, name='allvegetable'),
   path('search',views.search, name='search'),
]