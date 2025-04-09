from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>', views.product_list),
    path('product_list/', views.product_lists)

]