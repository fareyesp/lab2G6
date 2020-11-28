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
    path('registro/', views.RegistrationView.as_view(), name='register'),
    path('add_to_cart/<int:product_pk>',views.AddToCartView.as_view(), name='add-to-cart'),
    path('remove_from_cart/<int:product_pk>', views.RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('carrito/', views.PedidoDetailView.as_view(), name='pedido-detail'),
    path('checkout/<int:pk>', views.PedidoUpdateView.as_view(), name='pedido-update'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('complete_payment/', views.CompletePaymentView.as_view(), name='complete-payment'),
    path('pedidos_cliente/',views.PedidosClienteListView.as_view(), name='pedidos-cliente'),
    path('pedidos_cliente/<int:pk>',views.PedidosClienteDetailView.as_view(), name='pedidos-cliente-detail'),
    path('cancelar/<int:pedido_pk>',views.CancelarPedido.as_view(), name='cancelar')

]



