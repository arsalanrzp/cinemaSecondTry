app_name = 'accounts'
from django.urls import path
from accounts import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile/details', views.profile_details, name='profile_details'),
    path('signin/', views.registerform, name='signin')
]
