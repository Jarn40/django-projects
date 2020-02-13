from django.urls import path
from .views import list_products, create_product, update_product, delete_product

urlpatterns = [
    path('', list_products, name='list'),
    path('create', create_product, name='create'),
    path('update/<int:id>', update_product, name='update'),
    path('delete/<int:id>', delete_product, name='delete')

]
