import json
import string
from django.shortcuts import render, Http404
from django.core.paginator import Paginator

with open("CountriesApp/list_of_countries.json") as f:
    countries_data = json.load(f)

COUNTRIES_ON_PAGE = 20


# LANGUAGES_ON_PAGE = 20

# alphabet = string.ascii_uppercase # передаем алфавит в на страничку

def main(request):
    return render(request, 'index.html')


# Функция создание странички списка стран countries_list
def all_countries(request):
    # Создаем список и наполняем странами из .json
    country_names = []
    for country_dict in countries_data:
        country_names.append(country_dict["country"])

    # Блок отвечающий за пагинацию, кол-во всех стран на странице
    paginator = Paginator(country_names, COUNTRIES_ON_PAGE)
    page_number = request.GET.get('page')
    page_countries = paginator.get_page(page_number)
    return render(request, 'all_countries.html',
                  {"page_countries": page_countries})


# функция сзодания странички страны country/country_name
def country_page(request, country_name):
    country = {}

    for country_dict in countries_data:
        if country_dict["country"] == country_name:
            country["name"] = country_dict["country"]
            country["languages"] = country_dict["languages"]
            return render(request, 'country_page.html', {"country": country})
    raise Http404


# Функция создания странички languages (вывод всех языков)
def languages(request):
    langs = set()
    for country_dict in countries_data:
        langs.update(country_dict["languages"])

    return render(request, 'languages.html', {"languages": sorted(langs)})


# Функция для отображения стран при переходе по языку
def countries_filter_by_lang(request, language):
    # alphabet = string.ascii_uppercase
    country_names = []
    for country_dict in countries_data:
        if language in country_dict["languages"]:
            country_names.append(country_dict["country"])
    return render(request, 'all_countries.html', {"page_countries": country_names, })
