from django.shortcuts import render
from django.views.generic import *
from app.models import *
from app.mixins import *
# Create your views here.


class ProductMixin:
    model=Product
    fields=["name"]
    prefix="product"

class ProductCreateView(ProductMixin,CommonFormMixin, CreateView):
    pass
class ProductUpdateView(ProductMixin,CommonFormMixin, UpdateView):
    pass
class ProductDeleteView(ProductMixin,CommonDeleteMixin, DeleteView):
    pass
class ProductListView(ProductMixin,CommonListMixin,ListView):
    pass
class ProductDetailView(ProductMixin,CommonDetailMixin, DetailView):
    pass