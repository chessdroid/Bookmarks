from . import views
from django.urls import path, include
app_name='images'
urlpatterns = [
path('like/', views.image_like, name='like'),
   path('detail/<id>/<slug>/', views.image_detail, name='detail'),
    path('create/', views.image_create, name='create'),
   
   path('', views.image_list, name='list'),

]