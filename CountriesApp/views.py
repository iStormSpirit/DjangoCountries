import json
import string
from django.shortcuts import render, Http404
from django.core.paginator import Paginator

with open("CountriesApp/list_of_countries.json") as f:
    countries_data = json.load(f)

# Кол-во стран на странице
COUNTRIES_ON_PAGE = 10
# Кол-во стран в фильтре по букве /countries-list/?letter=D
COUNTRIES_ON_LETTER = 10
# Кол-во языков на странице /languages-list/?page=2
LANGUAGES_ON_PAGE = 10
# Кол-во языков в фильтре по букве languages-list/?page=2&letter=A
LANGUAGES_ON_LETTER = 10


def main(request):
    context = {'page_name': "HOME"}
    return render(request, 'index.html', context)


# Функция создание странички списка стран countries_list
def all_countries(request):
    alphabet = string.ascii_uppercase

    # Блок добавления стран список
    country_names = []
    for country_dict in countries_data:
        country_names.append(country_dict["country"])

    # Блок отвечающий за пагинацию всех стран на странице /countries-list/?page=3
    paginator = Paginator(country_names, COUNTRIES_ON_PAGE)
    page_number = request.GET.get('page')
    page_countries = paginator.get_page(page_number)

    # Блок фильтр проверки на letter
    letter = request.GET.get('letter')
    if letter:
        country_names = list(filter(lambda name: name[0] == letter, country_names))

        # Блок пагинации в нутри фильтра  /countries-list/?page=3&letter=A
        paginator = Paginator(country_names, COUNTRIES_ON_LETTER)
        page_number = request.GET.get('page')
        page_countries = paginator.get_page(page_number)
        # page_countries = country_names

    count = len(country_names)

    context = {'page_name': "Countries",
               "page_countries": page_countries,
               "alphabet": alphabet,
               "letter": letter,
               'total': count,
               }
    return render(request, 'all_countries.html', context)


# функция сзодания странички страны country/country_name
def country_page(request, country_name):
    country = {}
    for country_dict in countries_data:
        if country_dict["country"] == country_name:
            country["name"] = country_dict["country"]
            country["languages"] = country_dict["languages"]

    count = len(country["languages"])
    context = {'page_name': "Country: ",
               "country": country,
               'total': count,
               }
    return render(request, 'country_page.html', context)


# Функция создания списка языков
def all_languages(request):
    alphabet = string.ascii_uppercase

    # Блок создание множества уникальных языков
    languages = set()
    for languages_dict in countries_data:
        languages.update(languages_dict["languages"])

    # Блок добавления и сортировки уникальных языков в список из множества
    language_names = []
    for languages_dict in languages:
        language_names.append(languages_dict)
    language_names = sorted(language_names)

    # Блок пагинации всего списка языков
    paginator = Paginator(language_names, LANGUAGES_ON_PAGE)
    page_number = request.GET.get('page')
    page_languages = paginator.get_page(page_number)

    # Блок фильтр проверки на letter
    letter = request.GET.get('letter')
    if letter:
        language_names = list(filter(lambda name: name[0] == letter, language_names))

        # Блок пагинации в нутри фильтра
        paginator = Paginator(language_names, LANGUAGES_ON_LETTER)
        page_number = request.GET.get('page')
        page_languages = paginator.get_page(page_number)

    count = len(language_names)
    context = {'page_name': "Languages",
               "page_languages": page_languages,
               "alphabet": alphabet,
               "letter": letter,
               'total': count,
               }
    return render(request, 'all_languages.html', context)


# Функция создания странички языка
def language_page(request, language_name):
    # Блок добавления страны
    country_names = []
    for country_dict in countries_data:
        if language_name in country_dict["languages"]:
            country_names.append(country_dict["country"])

    # Блок отвечающий за пагинацию всех стран на странице языка/language/Russian?page=2
    paginator = Paginator(country_names, COUNTRIES_ON_PAGE)
    page_number = request.GET.get('page')
    page_language = paginator.get_page(page_number)

    count = len(country_names)
    context = {'page_name': "Language:",
               "language_name": language_name,
               "page_language": page_language,
               "country_names": country_names,
               'total': count,
               }
    return render(request, 'language_page.html', context)
