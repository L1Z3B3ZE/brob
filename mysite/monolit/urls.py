from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileBasket.as_view(), name='profile'),
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('products/', ProductsAllView.as_view(), name='all_products'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)