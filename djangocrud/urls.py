"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('aacongratulations1/', views.aacongratulations1, name="aacongratulations1"),
    path('aacongratulations2/', views.aacongratulations2, name="aacongratulations2"),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('signup/', views.signup),
    path('tasks/', views.tasks, name="tareas"),
    path('logout/', views.signout),
    path('signin/', views.signin), 
    path('tasks/create/', views.create_task),  
    path('tasks/<int:task_id/complete', views.complete_task, name="complete_task"),   
    path('tasks/<int:task_id>/', views.task_detail, name="task_detail"),
    path('aboutme/', views.about, name="aboutme"),  
    path('export-to-excel/', views.export_to_excel, name='export-to-excel'),
    path('vendor/', views.vistavendor, name='vendor'),
    path('crearproveedor/', views.crear_vendor, name="crearproveedor"),
    path('detalle/<int:pk>/', views.detalle_proveedor, name="detalle_proveedor"),
    path('productode/<int:pk>/', views.detalle_producto, name="detalle_producto"),
    path('exportexcelvendors/', views.export_vendors_to_excel, name='export-vendor-excel'),
    path('crearproducto/', views.crear_producto, name="crearproducto"),   
    path('productos/', views.productos, name='productos'),
    path('exportar_productos_excel/', views.exportar_productos_excel, name='exportar_productos_excel'),
    path('get_proveedor_details/', views.get_proveedor_details, name='get_proveedor_details'),
    path('eliminar-producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('eliminar-vendor/<int:pk>/', views.eliminar_vendor, name='eliminar_vendor'),
    path('eliminar-tarea/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('crear_orden_compra/', views.crear_orden_compra, name='crear_orden_compra'),
    path('ordenes/', views.ordenes, name='ordenes'),
    path('orden/<int:pk>/', views.detalle_orden_compra, name='detalle_orden_compra'),
    path('orden_compra/<int:pk>/', views.eliminar_orden_compra, name='eliminar_orden_compra'),
    path('exportar_compras_excel/', views.exportar_compraorden_excel, name='exportarcom'),
    path('crear_producto_proveedor/', views.crear_producto_proveedor, name='crear_producto_proveedor'),
    path('producto_vendor/', views.producto_vendor, name='producto_vendor'),
    path('buscar-productosproveedor/', views.buscar_productos_proveedor, name='buscar_productos_proveedor'),
    path('product_vendor/', views.product_vendor, name='product_vendor'),
    path('importar-datos/', views.importar_datos, name='importar_datos'),
    path('eliminar-productos/', views.eliminar_productos_general, name='eliminar_productos'),
    path('crear_nuevo_modelo/', views.crear_nuevo_modelo, name='crear_nuevo_modelo'),
    path('productos/modelos', views.productos_modelos, name='productos/modelos'),
    path('actualizar-datos/', views.actualizar_datos, name='actualizar_datos'),
    path('exportar_productos_vendor_excel/', views.exportar_productos_vendor_excel, name='exportar_productos_vendor_excel'),
    path('crear_persona/', views.crear_persona, name='crear_persona'),
    path('personas/', views.personas, name='personas'),
    path('eliminar-datos/', views.eliminar_datos, name='eliminar_datos'),
    path('productos/<str:nombre_modelo>/', views.productos_modelo, name='productos_modelo'),
    
# ------------------------------- Graficar -------------------------------# 
    path('grafica/', views.grafica, name='grafica'),
    path('chart/', views.chart, name='chart'),
    path('analisis-datos/', views.analisis_datos, name='analisis_datos'),

    


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    
    



