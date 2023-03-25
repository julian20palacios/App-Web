from django.forms import ModelForm
from django import forms
from .models import Task, Vendor, Productos, CompraOrden, ProductosProveedor, NuevoModelo, Persona

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Escribe un titulo'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control','placeholder':'Escribe una descripción'}),
            'important' : forms.CheckboxInput(attrs={'class' : 'form-check-input text-center'}),
        }

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la ciudad'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el país'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre de la compañía'}),
            'tax_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el ID fiscal'}),
            'credit_limit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el límite de crédito'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe la dirección'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el correo electrónico'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre de contacto'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el número de contacto'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la dirección del sitio web'}),
            'delivery_method': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el método de entrega'}),
            'potential_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la marca potencial'}),
            'potential_category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la categoría potencial'}),
            'price_opportunity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la oportunidad de precio'}),
            'featured_products': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe los productos destacados'}),
        }

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ["nombre_producto", "sku", "upc", "precio_usd", "categoria", "marca", "proveedor_sugerido", "arancel", "check_importante"]
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU'}),
            'upc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UPC'}),
            'precio_usd': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio en USD'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'proveedor_sugerido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Proveedor sugerido'}),
            'arancel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Arancel'}),
            'check_importante': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class CompraOrdenForm(forms.ModelForm):
    class Meta:
        model = CompraOrden
        exclude = ['correo_proveedor', 'direccion_proveedor', 'tax_id', 'ciudad_proveedor',
                   'nombre_contacto_proveedor', 'numero_contacto_proveedor', 'metodo_entrega_proveedor',
                   'upc', 'sku']
        widgets = {
            'numero_orden_compra': forms.TextInput(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'nombre_producto': forms.Select(attrs={'class': 'form-control'}),
            'precio_producto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProductosProveedorForm(forms.ModelForm):
    class Meta:
        model = ProductosProveedor
        fields = ['nombre', 'proveedor', 'precio', 'cantidad_disponible', 'upc']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio del producto'}),
            'cantidad_disponible': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad disponible'}),
            'upc': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'UPC'}),
        }
         
class NuevoModeloForm(forms.ModelForm):
    class Meta:
        model = NuevoModelo
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Articulo'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        try:
            nuevo_modelo = NuevoModelo.objects.get(nombre=nombre)
            # Si ya existe una instancia de NuevoModelo con ese nombre, lanzar una excepción
            raise forms.ValidationError('Ya existe un producto con ese nombre.')
        except NuevoModelo.DoesNotExist:
            pass
        return cleaned_data

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'edad', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'foto': forms.FileInput(attrs={'class': 'form-control-file'}),
        }   

class FiltroForm(forms.Form):
    proveedor = forms.ModelChoiceField(queryset=ProductosProveedor.objects.values_list('proveedor', flat=True).distinct(), empty_label=None)









