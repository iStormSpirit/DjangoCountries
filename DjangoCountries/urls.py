from django.urls import path
from CountriesApp import views

urlpatterns = [
    path('', views.main),   # Home page
    path('countries-list/', views.all_countries),  # Список всех стран c фильтром
    path('country/<str:country_name>', views.country_page),    # Информация по выбранной стране
    path('languages/', views.languages),  # Список всех языков
    path('countries-list/<str:language>', views.countries_filter_by_language),  # Переход по языкам

    # path('languages-list/', views.all_languages),  # Список всех языков (добавить фильтрацию и пагинацию)

]
