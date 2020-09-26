from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('productos',views.ProductListView.as_view(), name='product_list'),
    path('productos/<int:pk>',views.ProductDetailView.as_view(), name='product_detail'),
    path('proveedores',views.ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedores/<int:pk>',views.ProveedorDetailView.as_view(),name='proveedor_detail'),
    path('categoria',views.CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/<int:pk>',views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('localizacion',views.LocalizacionListView.as_view(), name='localizacion_list'),
    path('localizacion/<int:pk>',views.LocalizacionDetailView.as_view(), name='localizacion_detail'),
    path('registro/', views.RegistrationView.as_view(), name='register')


]

