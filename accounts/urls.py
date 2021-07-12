from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/loginpage.html'), name='login'),
    # path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile/details', views.profile_details, name='profile_details'),
    path('signin/', views.registerform, name='signin')
]
