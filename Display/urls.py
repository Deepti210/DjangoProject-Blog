from django.urls import path
from . import views

urlpatterns=[
    path('', views.display_hello_world),
    path('world', views.display_world),
    path('server',views.display_server),
    

]