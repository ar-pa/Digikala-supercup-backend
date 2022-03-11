from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.init),
    path('products/<int:user_id>/<str:lang>/<str:lat>/', views.products),
    path('shops/<int:user_id>/<str:lat>/<str:long>/', views.shops)
]
