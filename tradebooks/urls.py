from django.urls import path
from tradebooks import views

# added the index view here 
# all good - From Stanislva 

app_name = 'tradebooks'

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    # maybe we can use slug for individual products
    path('product/', views.product, name='product'),
    path('user/', views.user, name='user')
]
