from flask import Blueprint, url_for, redirect, request
import datetime

lab1 = Blueprint('lab1', __name__)

@lab1.route("/lab1")
def lab():
    return '''<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <main>
            <h1>Первая лабораторная работа</h1>

            <p>Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.</p>
            
            <h2>Список роутов</h2>
            <ul>
                <li><a href="''' + url_for('lab1.web') + '''">Web-сервер на Flask</a></li>
                <li><a href="''' + url_for('lab1.author') + '''">Об авторе</a></li>
                <li><a href="''' + url_for('lab1.image') + '''">Изображение</a></li>
                <li><a href="''' + url_for('lab1.counter') + '''">Счетчик посещений</a></li>
                <li><a href="''' + url_for('lab1.info') + '''">Перенаправление</a></li>
                <li><a href="''' + url_for('lab1.created') + '''">Создано успешно</a></li>
            </ul>
            <div>
                <a href="/">Вернуться на главную</a>
            </div>
        </main>
        <footer>
            Окачутин Вячеслав Владимирович, ФБИ-33, 3 курс, 2025
        </footer>
    </body>
</html>'''

@lab1.route("/lab1/web")
def web():
    return '''<!doctype html>
        <html>
            <body>
               <h1>web-сервер на flask</h1>
            </body>
        </html>''', 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }

@lab1.route("/lab1/author")
def author():
    name = "Окачутин Вячеслав Владимирович"
    group = "ФБИ-33"
    faculty = "ФБ"
    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href=""" + url_for('lab1.web') + """>web</a>
            </body>
        </html>"""

@lab1.route('/lab1/image')
def image():
    path = url_for("static", filename="flask.jpg")
    css_path = url_for("static", filename="lab1.css") 
    return """<!doctype html>
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href=""" + css_path + """>
        </head>
        <body>
            <h1>Flask</h1>
            <img src=""" + path + """>
        </body>
    </html>""", 200, {
        'Content-Language': 'ru',
        'X-Developer': 'Okachuchin Vyacheslav',
        'X-lab1-Version': '1.0',
        'X-Custom-Header': 'Flask-Lab-Work'
    }

count = 0

@lab1.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    reset_url = url_for("lab1.reset_counter")
    return """
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: """ + str(count) + """
        <hr>
        Дата и время: """ + str(time) + """<br>
        Запрошенный адрес: """ + url + """<br>
        Ваш IP адрес: """ + client_ip + """<br>
        <a href='""" + reset_url + """'>Сбросить счетчик</a>
    </body>
</html>
"""

@lab1.route('/lab1/reset_counter')
def reset_counter():
    global count
    count = 0
    return redirect(url_for('lab1.counter'))

@lab1.route("/lab1/info")
def info():
    return redirect(url_for('lab1.author'))

@lab1.route("/lab1/created")
def created():
    return """
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
""", 201