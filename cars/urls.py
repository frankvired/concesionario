from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cars'

urlpatterns = [
    # Public views
    path('', views.CarListView.as_view(), name='car_list'),
    path('coche/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('financiacion/', views.FinanciacionView.as_view(), name='financiacion'),
    path('vende-con-nosotros/', views.VendeConNosotrosView.as_view(), name='vende'),
    
    # Custom Auth views
    path('login/', auth_views.LoginView.as_view(template_name='cars/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Intraweb (Dashboard)
    path('intraweb/', views.IntrawebDashboardView.as_view(), name='intraweb_dashboard'),
    path('intraweb/nuevo/', views.CarCreateView.as_view(), name='car_create'),
    path('intraweb/editar/<int:pk>/', views.CarUpdateView.as_view(), name='car_update'),
    path('intraweb/eliminar/<int:pk>/', views.CarDeleteView.as_view(), name='car_delete'),
]
