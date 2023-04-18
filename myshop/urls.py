from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


app_name = 'myshop'

urlpatterns = [
    path('', cache_page(60)(views.product_list), name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail'),
]
