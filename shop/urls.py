from django.urls import path
from .views import ProdCat 


urlpatterns = [
    path('', ProdCat.as_view(),name='products'),
    path('<int:category_id>/', ProdCat.as_view(), name='product_list_by_category'),
]