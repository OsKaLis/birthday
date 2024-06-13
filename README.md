<div id="header" align="center">
  <h1>Проект birthday</h1>
</div>

## Что это за проект, какую задачу он решает, в чём его польза:
> [!NOTE]
> Cервис для отслеживания день рождения сотрудников!
> Что можно сделать:
> * 1] Зарегистрироваться в системе.
> * 2] Поиск нужного сотрудника.
> * 3] Подписаться и отписаться на интересного сотрудника. 
> * 4] Посмотреть на кого подписан.
> * 5] Посмотреть о ближайших днях рождениях сотрудников.
> * 6] Отправить поздравления сотруднику. 

## Cтек технологий:
<img src="https://img.shields.io/badge/Python:_-3.12.3-Green"> <img src="https://img.shields.io/badge/FastAPI:_-0.78.0-blue">
<img src="https://img.shields.io/badge/SQLAlchemy:_-1.4.36-yellow"> <img src="https://img.shields.io/badge/Alembic:_-1.7.7-red">
<img src="https://img.shields.io/badge/Poetry:_-1.8.3-yellow">


## Как развернуть проект на локальной машине.
> [!IMPORTANT]
> * 1 (Клонируем проект):git clone git@github.com:OsKaLis/birthday.git
> * 2 (Переходим в директорию проекта):cd birthday/
> * 3 (Запускаем виртуальное окружение из папки "birthday") :poetry shell
> * 4 (Устанавливаем установка зависимости для окружения):poetry install
> * 5 (Создаём фаил '.env')
>   ```
>   TITLE=Сервис о напоминание дне рождение сотрудника!!!
>   DATABASE_URL=sqlite+aiosqlite:///./birthday.db
>   APP_AUTHOR=ЮрийЮ.Ю.
>   AUTHOR_PASS=Z9C-w0u-DfP
>   DEADLINE_DATE=12.06.2024
>   DESCRIPTION=Сервис для отслеживания день рождения сотрудников! И информировать их об этом.
>   SECRET=GdeD%7mdy%KuBd%wukK%A3wd
>   FIRST_NAME=admiral
>   LAST_NAME=admiral
>   PATRONY=admiral
>   FIRST_SUPERUSER_EMAIL=admiral@admiral.com
>   FIRST_SUPERUSER_PASSWORD=admiral
>   ```
> * 6 (Запускаем) :uvicorn birthday.main:app --reload

## Планы по доработке:
* [1] - Дополнить работой фротендом (Бот тегергаама, Django) 
* [2] - Думою добавить работой с тасками 

## Документация для birthday:
> [!NOTE]
> ***`http://127.0.0.1:8000/docs#/`***

## Автор: Юшко Ю.Ю.
