from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('products/', views.products, name='products'),
    path('products/', views.ProductView.as_view(), name='products'),
    #path('produc_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/<int:id>/', views.product_detail, name='product_detail'),
    path('contact/',views.ContactForm.as_view(),name = 'contact'),
    path('about/',views.about,name = 'about'),

]


app_name = 'homeshop'