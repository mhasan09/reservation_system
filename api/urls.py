from django.urls import path
from . import views


urlpatterns = [
    path('api', views.api_endpoints, name='api_endpoints'),
    path('api/reservations/', views.get_all_reservations, name='get_all_reservations'),
    path('api/vacancies/', views.get_all_vacancies, name='get_all_vacancies'),
    path('data_load', views.load_vacancy_limit_data, name='load_vacancy_limit_data'),
    path('home', views.home, name='home'),
    path('save', views.save, name='save'),

]