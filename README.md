* Добавлена пагинация списка всех стран
* Переход на country/<name>
* Страничка с списком всех языков
* Переход между языком-страной-языком

## Развертывание проекта

1. Создать venv: python3 -m venv django_venv
2. Активировать: source django_venv/bin/activate
3. Установить зависимости: pip install -r requirements.txt
4. Применить миграции: python manage.py migrate
5. Запустить проект: python manage.py runserver
