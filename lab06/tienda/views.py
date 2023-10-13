from django.shortcuts import get_object_or_404, render
from .models import Producto
from .models import Categoria, Producto
# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.all()
    context = {'product_list': product_list, 'categorias':categorias}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'producto.html', {'producto': producto})
def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'layout.html', {'categorias': categorias})

def listar(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'listar.html', {'productos': productos, 'categoria': categoria})

