from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('setup-household/', views.setup_household, name='setup_household'),
    path('add-energy/', views.add_energy_data, name='add_energy_data'),
    path('add-transport/', views.add_transport_data, name='add_transport_data'),
    path('add-diet/', views.add_diet_data, name='add_diet_data'),
    path('add-waste/', views.add_waste_data, name='add_waste_data'),
    path('bulk-entry/', views.bulk_data_entry, name='bulk_data_entry'),
    path('calculate/', views.calculate_footprint, name='calculate_footprint'),
    path('calculate/<str:month>/', views.calculate_footprint, name='calculate_footprint_month'),
    path('tips/', views.tips, name='tips'),
    path('reports/', views.reports, name='reports'),
    path('api/footprint-data/', views.api_footprint_data, name='api_footprint_data'),
    path('setup-sample-data/', views.setup_sample_data, name='setup_sample_data'),
] 