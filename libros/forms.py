from django import forms
from .models import Libros, Stock, Biblioteca

class LibrosForm(forms.ModelForm):

    class Meta:
        # Importo el modelo con el que quiero trabajar
        model = Libros
        
        # Los campos a los que quiero ingresar datos desde el template
        fields = ['nombre', 'autor', 'paginas']

        # Creo un diccionario con configuraciónes para los imput en el template
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Libro', 'autofocus':'autofocus'}),
            'autor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Autor del Libro'}),
            'paginas': forms.TextInput(attrs={'class':'form-control', 'type':'number', 'placeholder':'Páginas'}),
        }

        labels = {
            # Que ordene por el campo nombre
            'nombre':''
        }

# Estoy pensando en que si un Form puede heradar de otro?
# EJEMPLO: class StockForm(LibrosForm):
class StockForm(forms.ModelForm):

    class Meta:
        # Importo el modelo con el que quiero trabajar
        model = Stock
        
        # Los campos a los que quiero ingresar datos desde el template
        fields = ['libro', 'stock']

        # Creo un diccionario con configuraciónes para los imput en el template
        widgets = {
            #'libro': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Libro', 'autofocus':'autofocus'}),
            'libro': forms.Select(attrs={'class':'form-control', 'type':'select'}),
            'stock': forms.TextInput(attrs={'class':'form-control', 'type':'number', 'placeholder':'Páginas'}),
        }


class BibliotecaForm(forms.ModelForm):

    class Meta:
        # Importo el modelo con el que quiero trabajar
        model = Biblioteca
        
        # Los campos a los que quiero ingresar datos desde el template
        fields = ['nombre', 'direccion']

        # Creo un diccionario con configuraciónes para los imput en el template
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la biblioteca', 'autofocus':'autofocus'}),
            'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'}),
        }

        labels = {
            # Que ordene por el campo nombre
            'nombre':''
        }
