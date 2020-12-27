# Architecture_Patterns
Домашние задания по курсу "Архитектура и шаблоны проектирования на Python"

Запуск проекта:
gunicorn main:app

## Урок 1. Паттерны web-представления
`gunicorn main:app`
0. Создать репозиторий для нового проекта (gitlab, github, ...)
1. С помощью `uwsgi` или `gunicorn` запустить пример `simple_wsgi.py`, проверить что он работает (Эти библиотеки работают на linux системах, документацию по ним можно найти в дополнительных материалах)
2. Написать свой wsgi фреймворк использую паттерны `page controller` и `front controller`.  
    Описание работы фреймворка:  
    * возможность отвечать на get запросы пользователя (код ответа + html страница)  
    * для разных url - адресов отвечать разными страницами  
    * page controller - возможность без изменения фреймворка добавить view для обработки нового адреса  
    * front controller - возможность без изменения фреймворка вносить изменения в обработку всех запросов  
3. Реализовать рендеринг страниц с помощью шаблонизатора `jinja2`. Документацию по этой библиотеке можно найти в дополнительных материалах
4. Добавить любый полезный функционал в фреймворк, например обработку наличия (отсутствия) слеша в конце адреса, ...
5. Добавить для демонстрации 2 любые разные страницы (например главная и about или любые другие)
6. Сдать дз в виде ссылки на репозиторий
7. В readme указать пример как запустить фреймворк с помощью uwsgi и/или gunicorn

## Урок 2. Архитектура python-приложений
1. Добавить в свой wsgi-фреймворк возможность обработки post-запроса
2. Добавить в свой wsgi-фреймворк возможность получения данных из post запроса
3. Дополнительно можно добавить возможность получения данных из get запроса
4. В проект добавить страницу контактов на которой пользователь может отправить нам сообщение (пользователь вводит тему сообщения, его текст, свой email)
5. После отправки реализовать сохранение сообщения в файл, либо вывести сообщение в терминал (базу данных пока не используем)

## Урок 3. Принципы проектирования
1. Внести изменения в wsgi-фреймворк, которые позволят использовать механизм наследования и включения шаблонов
2. Создать базовый шаблон для всех страниц сайта
3. Если нужно создать один или несколько включенных шаблонов
4. Добавить на сайт меню, которое будет отображаться на всех страницах
5. Улучшить имеющиеся страницы с использованием базовых и включенных шаблонов
6. Проверить что фреймворк готов для дальнейшего использования при желании добавить какой либо полезный функционал

## Урок 4. Порождающие паттерны
1. Добавить следующий функционал:
   * Создание категории курсов
   * Вывод списка категорий
   * Создание курса
   * Вывод списка курсов
2. Далее можно сделать всё или одно на выбор, применив при этом один из порождающих паттернов, либо аргументировать
   почему данные паттерны не были использованы:
   * На сайте могут быть курсы разных видов: офлайн (в живую) курсы (для них указывается адрес проведения) и онлайн
     курсы (вебинары), для них указывается вебинарная система. Также известно что в будущем могут добавиться новые виды
     курсов
   * Реализовать простой логгер (не используя сторонние библиотеки). У логгера есть имя. Логгер с одним и тем же именем
     пишет данные в один и тот же файл, а с другим именем в другой
   * Реализовать страницу для копирования уже существующего курса (Для того чтобы снова с нуля не создавать курс, а
     скопировать существующий и немного отредактировать)

## Урок 5. Структурные паттерны
1. Добавить декоратор для добавления связки `url-view` в приложение, чтобы можно было добавлять url-ы, как в фреймворке
   Flask `@app(‘/some_url/’)`
2. Добавить декоратор `@debug`, для `view`, если мы указываем данный декоратор над view, то в терминал выводятся
   название функции и время ее выполнения
3. Добавить подкатегорий. Т.е. категория курса может входит в другую категорию, а может не входить и вложенность может
   быть любая. Например: Программирование->Web->Python->Django. После на страницу списка категорий добавить вывод
   количества курсов в каждой из категорий. Например Программирование - 10, Web - 5, Python - 3, …
4. Добавить 2 новых вида wsgi-application. Первый - логирующий (такой же как основной, только он для каждого запроса
   выводит информацию (тип запроса и параметры) в консоль. Второй - фейковый (на все запросы пользователя отвечает “200
   OK”, “Hello from Fake”)
5. По желанию можно добавить любой другой полезный функционал

## Урок 6. Поведенческие паттерны
1. Реализовать создание студента (регистрация). Список студентов. Запись студента на курс.
2. Далее можно сделать всё или одно на выбор, применив при этом один из структурных паттернов, либо аргументировать почему данные паттерны не были использованы:
* Создать страницу для изменения курса. После изменения отправлять уведомления всем студентам на курсе по sms, email (для имитации можно просто выводить сообщения в консоль). Также известно, что в будущем способов уведомления будет больше
* Добавить возможность применять цикл for к объекту категории курса (в каждой итерации получаем курс) и объекта курса (в каждой итерации получаем студента). Например for student in course: … for course in group
* Создать api для курсов. По определенному адресу выводить не веб-страницу, а отдавать пользователю данные о списке курсов в формате json
* Улучшить логгер (или добавить если его нет). Добавить в логгер возможность писать в файл, в консоль. Также известно что в будущем вариантов сохранения может быть еще больше
* Реализовать CBV (Class Based VIews). Возможность создавать view в виде класса (по аналогии с Django). И убрать таким образом часть дублирования во view
