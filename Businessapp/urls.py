from django.contrib import admin
from django.urls import path
from Businessapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    # path('inner/', views.inner, name='inner'),
    # path('about/', views.about, name='about'),
    # path('doctors/', views.doctors, name='doctors'),
    path('addproducts/', views.add, name='addproducts'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('pay/',views.pay,name = 'pay'),
    path('token/',views.token,name = 'token'),
    path('stk/',views.stk,name = 'stk'),
]


