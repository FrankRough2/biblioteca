from django.views.generic.list import ListView          # Para listar el contenido de un modelo
from django.views.generic.detail import DetailView      # Para ver el detalle
from django.views.generic.edit import CreateView        # Para crear
from django.views.generic.edit import UpdateView        # Para actualizar
from django.views.generic.edit import DeleteView        # Para borrar
from django.views.generic.base import TemplateView      # Para crear un template
from django.urls import reverse, reverse_lazy           # Se utiliza para redireccionar páginas
from .models import Libros, Stock, Biblioteca
from .forms import LibrosForm, BibliotecaForm, StockForm


# Class que muestra una lista en un template mediante un form
# Apunta al template libros_list.html
class LibroListView(ListView):
    # Importo el modelo con el que quiero trabajar
    model = Libros

    # Paginación de 10
    paginate_by = 10

    # Pasamos la variable stock_list que pertences al modelo Stock
    def get_context_data(self, **kwargs):
        context = super(LibroListView, self).get_context_data(**kwargs)
        context['stock_list'] = Stock.objects.all()
        context['biblioteca_list'] = Biblioteca.objects.all()
        return context


# Class que muestra el detalle en un template de un libro en particular
# Apunta al template libros_detail.html
class LibrosDetailView(DetailView):
    # Importo el modelo con el que quiero trabajar
    model = Libros


# Class que crea mediante un formulario en un template un libro en particular
# Apunta al template libros_form.html
class LibrosCreate(CreateView):
    # Importo el modelo con el que quiero trabajar
    model = Libros

    # Pasamos el formulario del archivo forms.py
    form_class = LibrosForm

    # Indicamos que luego de crear un libro busque la página libros_list
    success_url = reverse_lazy('libros_list')



# Class para editar un libro mediante un formulario en un template
# Apunta al template libros_update_form.html
class LibrosUpdate(UpdateView):
    # Importo el modelo con el que quiero trabajar
    model = Libros

    # Pasamos el formulario del archivo forms.py
    form_class = LibrosForm

    template_name_suffix = '_update_form'

    # Redireccionar luego de editar
    def get_success_url(self):
        return reverse_lazy('libros_list')



# --- /// B I B L I O T E C A /// ---
# Class que crea mediante un formulario en un template un libro en particular
# Apunta al template biblioteca_form.html
class BibliotecaCreate(CreateView):
    # Importo el modelo con el que quiero trabajar
    model = Biblioteca

    # Pasamos el formulario del archivo forms.py
    form_class = BibliotecaForm

    # Indicamos que luego de crear un libro busque la página libros_list
    success_url = reverse_lazy('libros_list')



# --- /// S T O C K /// ---
# Class que crea mediante un formulario en un template un libro en particular
# Apunta al template stock_form.html
class StockCreate(CreateView):
    # Importo el modelo con el que quiero trabajar
    model = Stock

    # Pasamos el formulario del archivo forms.py
    form_class = StockForm

    # Indicamos que luego de crear un libro busque la página libros_list
    success_url = reverse_lazy('libros_list')



class stockDetailView(DetailView):

    model = Stock
