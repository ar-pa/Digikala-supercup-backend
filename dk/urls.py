from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.init),
    path('products/<int:user_id>/<int:lang>/<int:lat>/', views.products),
    path('shops/<int:user_id>/<int:lang>/<int:lat>/', views.shops)
]
