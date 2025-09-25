from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return '''<!doctype html>
        <html>
            <head>
                <title>НГТУ, ФБ, Лабораторные работы</title>
            </head>
            <body>
                <header>НГТУ, ФБ, WEB-программирование, часть 2.</header> 
                <h1>Список лабораторных</h1>
                <ul>
                    <li><a href='/lab1'>Первая лабораторная</a></li>
                </ul>
                <footer>
                    Окачутин Вячеслав Владимирович, ФБИ-33, 3 курс, 2025
                </footer>
            </body>
        </html>'''

@app.route("/lab1")
def lab1():
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
            
            <a href="''' + url_for('index') + '''">Вернуться на главную</a>
            
            <h2>Список роутов</h2>
            <ul>
                <li><a href="''' + url_for('web') + '''">Web-сервер на Flask</a></li>
                <li><a href="''' + url_for('author') + '''">Об авторе</a></li>
                <li><a href="''' + url_for('image') + '''">Изображение</a></li>
                <li><a href="''' + url_for('counter') + '''">Счетчик посещений</a></li>
                <li><a href="''' + url_for('info') + '''">Перенаправление</a></li>
            </ul>
        </main>
        <footer>
            Окачутин Вячеслав Владимирович, ФБИ-33, 3 курс, 2025
        </footer>
    </body>
</html>'''

@app.route("/lab1/web")
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

@app.route("/lab1/author")
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
                <a href='/web'>web</a>
            </body>
        </html>"""

@app.route('/lab1/image')
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
    </html>"""

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    reset_url = url_for("reset_counter")
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

@app.route('/reset_counter')
def reset_counter():
    global count
    count = 0
    return redirect(url_for('counter'))

@app.route("/lab1/info")
def info():
    return redirect("/author")

@app.route("/lab1/created")
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

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404