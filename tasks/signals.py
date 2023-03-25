from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductosProveedor, NuevoModelo

@receiver(post_save, sender=ProductosProveedor)
def actualizar_nuevos_modelos(sender, instance, created, **kwargs):
    if created:
        # Si se creó un nuevo objeto ProductosProveedor, buscar los nuevos modelos relacionados
        nuevos_modelos = NuevoModelo.objects.filter(nombre=instance.nombre)
        for modelo in nuevos_modelos:
            modelo.proveedor = instance.proveedor
            modelo.precio = instance.precio
            modelo.cantidad_disponible = instance.cantidad_disponible
            modelo.upc = instance.upc
            modelo.save()
    else:
        # Si se actualizó un objeto ProductosProveedor, buscar los nuevos modelos relacionados
        nuevos_modelos = NuevoModelo.objects.filter(nombre=instance.nombre, proveedor=instance.proveedor, precio=instance.precio, cantidad_disponible=instance.cantidad_disponible, upc=instance.upc)
        for modelo in nuevos_modelos:
            modelo.proveedor = instance.proveedor
            modelo.precio = instance.precio
            modelo.cantidad_disponible = instance.cantidad_disponible
            modelo.upc = instance.upc
            modelo.save()