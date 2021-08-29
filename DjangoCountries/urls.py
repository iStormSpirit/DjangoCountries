from django.urls import path, include
from CountriesApp import views

urlpatterns = [
    path('', views.main, name="home"),   # Home page
    path('countries-list/', views.all_countries, name="countries-list"),  # Список всех стран c фильтром
    path('country/<str:country_name>', views.country_page),     # Информация по выбранной стране
    path('languages-list/', views.all_languages, name="languages-list"),  # Список всех языков (добавить фильтрацию и пагинацию)
    path('language/<str:language_name>', views.language_page),     # Информация по выбранном языке

]
