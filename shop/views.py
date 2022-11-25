from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.views.generic import ListView
from django.db.models import Count

class ProdCat(ListView):
    model = Product

    def get(self,request, category_id=None):
        category = None
        categories = Category.objects.all()
        products = None
        if category_id != None:
            category = get_object_or_404(Category, id = category_id)
            products = Product.objects.filter(category = category)
        else:
            products = Product.objects.all()
        
        return  render(request,"products.html",{'categories':categories, 'products':products})
