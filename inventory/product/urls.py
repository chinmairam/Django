from django.urls import path
from . import views


# path for various actions of the product app
urlpatterns = [
    path('', views.archive, name='archive'),
    path('index', views.index, name='index'),
    path('addproduct', views.create_product, name='addproduct'),
    path('<int:prod_id>/', views.detail, name='detail'),
    path('csv', views.generate_csv, name='csv'),
]
