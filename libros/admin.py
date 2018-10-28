from django.contrib import admin
from .models import Libros,Stock

class StockInline(admin.TabularInline):
    model = Stock

@admin.register(Libros)
class LibrosAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    inlines = [StockInline]
admin.site.register(Stock)
