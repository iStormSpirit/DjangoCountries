import json
import string
from django.shortcuts import render, Http404
from django.core.paginator import Paginator

with open("CountriesApp/list_of_countries.json") as f:
    countries_data = json.load(f)

# Кол-во стран на странице /countries-list/
COUNTRIES_ON_PAGE = 15
# Кол-во стран в фильтре по букве /countries-list/?letter=D
COUNTRIES_ON_LETTER = 10
# Кол-во языков на странице
LANGUAGES_ON_PAGE = 15
# Кол-во языков в фильтре по букве
LANGUAGES_ON_LETTER = 10


def main(request):
    return render(request, 'index.html')


# Функция создание странички списка стран countries_list
def all_countries(request):
    alphabet = string.ascii_uppercase
    country_names = []
    for country_dict in countries_data:
        country_names.append(country_dict["country"])

    # Блок отвечающий за пагинацию всех стран на странице /countries-list/?page=3
    paginator = Paginator(country_names, COUNTRIES_ON_PAGE)
    page_number = request.GET.get('page')
    page_countries = paginator.get_page(page_number)

    # Блок проверки на фильтр letter
    letter = request.GET.get('letter')
    if letter:
        country_names = list(filter(lambda name: name[0] == letter, country_names))

        # Блок пагинации в нутри фильтра  /countries-list/?page=3&letter=A
        paginator = Paginator(country_names, COUNTRIES_ON_LETTER)
        page_number = request.GET.get('page')
        page_countries = paginator.get_page(page_number)
    return render(request, 'all_countries.html',
                  {"page_countries": page_countries, "alphabet": alphabet, "letter": letter})


# функция сзодания странички страны country/country_name
def country_page(request, country_name):
    country = {}

    for country_dict in countries_data:
        if country_dict["country"] == country_name:
            country["name"] = country_dict["country"]
            country["languages"] = country_dict["languages"]
            return render(request, 'country_page.html', {"country": country})
    raise Http404


# Функция для отображения стран при переходе по языку
def countries_filter_by_language(request, language):
    country_names = []
    for country_dict in countries_data:
        if language in country_dict["languages"]:
            country_names.append(country_dict["country"])
    return render(request, 'all_countries.html', {"page_countries": country_names})


def all_languages(request):
    alphabet = string.ascii_uppercase

    # Блок создание множества уникальных языков
    languages = set()
    for languages_dict in countries_data:
        languages.update(languages_dict["languages"])

    # Блок добавления и сортировки уникальных языков в список из множества
    language_names = []
    for i in languages:
        language_names.append(i)
    language_names = sorted(language_names)

    # Блок пагинации всего списка языков
    paginator = Paginator(language_names, LANGUAGES_ON_PAGE)
    page_number = request.GET.get('page')
    page_languages = paginator.get_page(page_number)

    # Блок проверки на фильтр letter
    letter = request.GET.get('letter')
    if letter:
        language_names = list(filter(lambda name: name[0] == letter, language_names))

        # Блок пагинации в нутри фильтра
        paginator = Paginator(language_names, LANGUAGES_ON_LETTER)
        page_number = request.GET.get('page')
        page_languages = paginator.get_page(page_number)

    return render(request, 'all_languages.html',
                  {"page_languages": page_languages, "alphabet": alphabet,"letter": letter})
