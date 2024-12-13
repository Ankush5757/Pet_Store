from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('savetocart/<int:id>/',views.savetocart, name='savetocart'),
    path('mycart/',views.mycart, name='mycart'),
    path('checkout/',views.checkout, name='checkout'),
    path('orders/',views.orders, name='orders'),
    path('pets/',views.pets, name='pets'),
    path('profile/',views.profile, name='profile'),
    path('wishlist/',views.wishlist, name='wishlist'),
    path('remove_pet/<int:id>/',views.remove_pet, name='remove_pet'),
    path('search/',views.search, name='search'),
    path('update_quantity/<int:id>/<str:action>/',views.update_quantity, name='update_quantity'),
    path('buyapet/<int:id>/', views.buyapet, name='buyapet'),
    path('buyallpets/', views.buyallpets, name='buyallpets'),
    path('payment/<int:amount>/',views.payment,name="payment"),    
    path('success/<int:amount>/<int:id>/<str:payment_id>/<str:address>/<int:session>/',views.success,name="success"),
    path('expensive_pets',views.expensive_pets,name="expensive_pets"),
    

]