# nolabel-backend

# badges
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=nolabel-tech_notable-backend&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=nolabel-tech_notable-backend)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=nolabel-tech_notable-backend&metric=bugs)](https://sonarcloud.io/summary/new_code?id=nolabel-tech_notable-backend)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=nolabel-tech_notable-backend&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=nolabel-tech_notable-backend)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=nolabel-tech_notable-backend&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=nolabel-tech_notable-backend)

# Проект sm2

Проект sm2 — это веб-приложение на базе Django, предназначенное для управления пользователями и сообщениями между ними. Этот проект включает в себя пользовательскую аутентификацию, отправку сообщений и функции администрирования.

## Содержание
- [Функции](#функции)
- [Установка](#установка)
- [Конфигурация](#конфигурация)
- [Использование](#использование)
- [API Эндпоинты](#api-эндпоинты)

## Функции

- Регистрация и аутентификация пользователей.
- Отправка сообщений между пользователями.
- Административная панель для управления пользователями и сообщениями.
- Генерация уникальных токенов для пользователей.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/ваш-репозиторий.git
    cd sm2
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv env
    source env/bin/activate  # для Windows: env\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции базы данных:

    ```bash
    python manage.py migrate
    ```

5. Создайте суперпользователя:

    ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

## API Эндпоинты

### Регистрация пользователя

- **URL:** `/api/register/`
- **Метод:** `POST`
- **Параметры:**
  - `email` (строка): Электронная почта пользователя.
  - `username` (строка): Имя пользователя.
  - `unique` (строка): Уникальный идентификатор.
  - `password` (строка): Пароль пользователя.

### Аутентификация пользователя

- **URL:** `/api/login/`
- **Метод:** `POST`
- **Параметры:**
  - `username` (строка): Имя пользователя.
  - `password` (строка): Пароль пользователя.

### Отправка сообщения

- **URL:** `/api/send_message/`
- **Метод:** `POST`
- **Параметры:**
  - `unique` (строка): Уникальный идентификатор получателя.
  - `message` (строка): Содержание сообщения.
  - `from_user` (строка): Уникальный идентификатор отправителя.

### Проверка сообщений

- **URL:** `/api/check_messages/<unique>/`
- **Метод:** `GET`
- **Описание:** Проверка непрочитанных сообщений для пользователя с указанным уникальным идентификатором.

## Автор

Проект создан Султановым Халилом.


