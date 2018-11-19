from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    #path('', views.index, name='index'),
    url(r'^pensum/nuevo/$', views.pensum_nuevo, name='pensum_nuevo'),
    #path('factura/lista', views.factura_lista, name='factura_lista'),
    #path('factura/<int:pk>/editar/', views.factura_editar, name='factura_editar'),
    #url(r'^factura/(?P<pk>\d+)/remove/$', views.factura_remove, name='factura_remove'),
    #path('factura/<int:pk>/', views.factura_detalle, name='factura_detalle'),
    ]
