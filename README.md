# Django Tree Menu App

Это Django-приложение предоставляет древовидное меню, которое можно настроить через админку Django и отобразить на веб-странице с использованием шаблонного тега.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone git@github.com:mir21bek/UpTrader.git
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Примените миграции:

    ```bash
    python manage.py migrate
    ```

4. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

5. Перейдите по адресу [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) для добавления пунктов меню через админку Django.

## Использование

1. В вашем шаблоне добавьте следующие строки для отображения древовидного меню:

    ```html
    {% load menu_tags %}

    {% draw_menu 'main_menu' %}
    <ul>
      {% for item in menu_items %}
        <li{% if item.url == current_path or item.named_url == current_path %} class="active"{% endif %}>{{ item.title }}
          {% if item.children.all %}
            <ul>
              {% for child in item.children.all %}
                <li{% if child.url == current_path or child.named_url == current_path %} class="active"{% endif %}>{{ child.title }}</li>
              {% endfor %}
            </ul>
          {% endif %}
        </li>
      {% endfor %}
    </ul>
    ```

    Где `'main_menu'` - это название вашего меню.

2. Настройте пункты меню через админку Django.
