from django.contrib import admin
from .models import Task, Vendor, Productos, CompraOrden, ProductosProveedor, NuevoModelo, Persona

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )
admin.site.register(Task, TaskAdmin)

class VendorAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email', 'contact_name', 'is_important', 'is_purchased']
    list_filter = ['is_important', 'is_purchased']
    search_fields = ['company_name', 'email', 'contact_name']
admin.site.register(Vendor, VendorAdmin)

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'sku', 'precio_usd', 'categoria', 'marca', 'proveedor_sugerido', 'arancel', 'check_importante')
    list_filter = ('categoria', 'marca', 'proveedor_sugerido', 'check_importante')
    search_fields = ('nombre_producto', 'sku', 'proveedor_sugerido')
admin.site.register(Productos, ProductosAdmin)

class CompraOrdenAdmin(admin.ModelAdmin):
    list_display = ('numero_orden_compra', 'proveedor', 'nombre_producto', 'precio_producto', 'correo_proveedor', 'direccion_proveedor', 'tax_id', 'ciudad_proveedor', 'nombre_contacto_proveedor', 'numero_contacto_proveedor', 'metodo_entrega_proveedor', 'upc', 'sku')
    list_filter = ('proveedor', 'nombre_producto')
    search_fields = ('numero_orden_compra', 'proveedor__nombre_proveedor', 'nombre_producto__nombre_producto')
admin.site.register(CompraOrden, CompraOrdenAdmin)

class ProductosProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proveedor', 'precio', 'cantidad_disponible', 'upc')
    list_filter = ('proveedor',)
    search_fields = ('nombre', 'proveedor')
admin.site.register(ProductosProveedor, ProductosProveedorAdmin)


class NuevoModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proveedor', 'precio', 'cantidad_disponible', 'upc')
    list_filter = ('proveedor',)
    search_fields = ('nombre', 'proveedor')
admin.site.register(NuevoModelo, NuevoModeloAdmin)

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'foto_thumbnail')    
    def foto_thumbnail(self, obj):
        return '<img src="%s" width="100" height="100"/>' % obj.foto.url

    foto_thumbnail.allow_tags = True   
admin.site.register(Persona, PersonaAdmin)

