from django.urls import path
from CountriesApp import views

urlpatterns = [
    path('', views.main),# Home page
    path('countries-list/', views.all_countries),  # Список всех стран
    path('country/<str:country_name>', views.country_page),  # Информация по выбранной стране
    path('languages/', views.languages),# Список всех языков
    path('countries-list/<str:language>', views.countries_filter_by_lang), # Переход по языкам


    # path('countries-list/<str:word>', views.countries_filter_by_word),
]
