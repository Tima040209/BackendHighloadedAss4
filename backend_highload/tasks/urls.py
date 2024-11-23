from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('account/', include('two_factor.urls', 'two_factor')),
]
