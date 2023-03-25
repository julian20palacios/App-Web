from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import RegexValidator


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecomplated = models.DateTimeField(null=True)
    important = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)   

    def _str_(self):
        return self.title + " by " + self.user.username

class Vendor(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=50)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    email = models.EmailField()
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    website = models.URLField()
    delivery_method = models.CharField(max_length=100)
    potential_brand = models.CharField(max_length=100)
    potential_category = models.CharField(max_length=100)
    price_opportunity = models.CharField(max_length=10)
    featured_products = models.TextField()
    credit_check = models.BooleanField(default=False)
    document_check = models.BooleanField(default=False)
    factoring_check = models.BooleanField(default=False)   
    is_important = models.BooleanField(default=False)
    is_purchased = models.BooleanField(default=False)
    
    def _str_(self):
        return self.company_name

class Productos(models.Model):
    nombre_producto = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    upc = models.CharField(max_length=255)
    precio_usd = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    proveedor_sugerido = models.CharField(max_length=255)
    arancel = models.DecimalField(max_digits=10, decimal_places=2)
    check_importante = models.BooleanField()
    
    def _str_(self):
        return self.nombre_producto

class CompraOrden(models.Model):
    numero_orden_compra = models.CharField(max_length=255)
    proveedor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    nombre_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Setear los valores de los campos heredados al seleccionar el proveedor y el producto
        self.correo_proveedor = self.proveedor.email
        self.direccion_proveedor = self.proveedor.address
        self.tax_id = self.proveedor.tax_id
        self.ciudad_proveedor = self.proveedor.city
        self.nombre_contacto_proveedor = self.proveedor.contact_name
        self.numero_contacto_proveedor = self.proveedor.contact_number
        self.metodo_entrega_proveedor = self.proveedor.delivery_method
        self.upc = self.nombre_producto.upc
        self.sku = self.nombre_producto.sku

        super().save(*args, **kwargs)

    # Campos heredados del proveedor
    correo_proveedor = models.EmailField(editable=False)
    direccion_proveedor = models.TextField(editable=False)
    tax_id = models.CharField(max_length=50, editable=False)
    ciudad_proveedor = models.CharField(max_length=100, editable=False)
    nombre_contacto_proveedor = models.CharField(max_length=100, editable=False)
    numero_contacto_proveedor = models.CharField(max_length=20, editable=False)
    metodo_entrega_proveedor = models.CharField(max_length=100, editable=False)
    
    # Campos heredados del producto
    upc = models.CharField(max_length=255, editable=False)
    sku = models.CharField(max_length=255, editable=False)

    def _str_(self):
        return self.numero_orden_compra

class ProductosProveedor(models.Model):
    nombre = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad_disponible = models.IntegerField()
    upc = models.IntegerField()
    
    def _str_(self):
        return self.nombre
       
class NuevoModelo(models.Model):
    nombre = models.CharField(max_length=100, default="Nombre predefinido")
    proveedor = models.CharField(max_length=100, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    cantidad_disponible = models.IntegerField(blank=True, null=True)
    upc = models.IntegerField(blank=True, null=True)

    def _str_(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.proveedor or not self.precio or not self.cantidad_disponible or not self.upc:
            # Si falta algún dato, buscar el producto con el precio más bajo
            producto_menor_precio = ProductosProveedor.objects.filter(nombre=self.nombre).order_by('precio').first()
            if producto_menor_precio:
                self.proveedor = producto_menor_precio.proveedor
                self.precio = producto_menor_precio.precio
                self.cantidad_disponible = producto_menor_precio.cantidad_disponible
                self.upc = producto_menor_precio.upc
        super(NuevoModelo, self).save(*args, **kwargs)

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    foto = models.ImageField(upload_to='fotos')
    
    def _str_(self):
        return self.nombre
    
