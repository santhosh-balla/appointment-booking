from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home'),
    path('register/company/', views.register_company, name='register_company'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('test-base/', views.test_template),
]

urlpatterns += [
    path('logout-test/', lambda request: HttpResponse("Test route works")),
]
