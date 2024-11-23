from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.auth_login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
