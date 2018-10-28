from django.urls import path
from .views import  LibroListView, LibrosDetailView, LibrosCreate, LibrosUpdate, BibliotecaCreate, StockCreate, stockDetailView


libros_patterns = [
    path('', LibroListView.as_view(), name='libros_list'),
    path('libros_detail/<int:pk>/<slug:slug>/', LibrosDetailView.as_view(), name='libros_detail'),
    path('libros_create/', LibrosCreate.as_view(), name='libros_create'),
    path('libros_update/<int:pk>', LibrosUpdate.as_view(), name='libros_update'),
    path('biblioteca_create/', BibliotecaCreate.as_view(), name='biblioteca_create'),
    path('stock_create/<int:pk>', StockCreate.as_view(), name='stock_create'),

#### DetailView for Stock 
    path('stock_detail/<int:pk>',stockDetailView.as_view(),name='stock-detail'),
]
