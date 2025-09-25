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
    css_path = url_for("static", filename="error.css")
    image_path = url_for("static", filename="404.jpg")
    return f"""
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
        <title>Страница не найдена</title>
    </head>
    <body>
        <div class="container">
            <h1>Ой! Кажется, мы потеряли эту страницу...</h1>
            <div class="error-code">404</div>
            <img src="{image_path}" alt="Потерянная страница">
            <p>Запрашиваемая страница куда-то пропала. Возможно, она переехала или никогда не существовала.</p>
            <p>Попробуйте вернуться на <a href="/">главную страницу</a> или проверьте правильность адреса.</p>
            <div class="fun-fact">
                <strong>Интересный факт:</strong> В интернете ежедневно теряется более 1 миллиона страниц!
            </div>
        </div>
    </body>
</html>
""", 404
@app.route('/400')
def bad_request():
    return """
<!doctype html>
<html>
    <body>
        <h1>400 Bad Request</h1>
        <p>Сервер не может обработать запрос из-за клиентской ошибки</p>
    </body>
</html>
""", 400

@app.route('/401')
def unauthorized():
    return """
<!doctype html>
<html>
    <body>
        <h1>401 Unauthorized</h1>
        <p>Требуется аутентификация для доступа к ресурсу</p>
    </body>
</html>
""", 401

@app.route('/402')
def payment_required():
    return """
<!doctype html>
<html>
    <body>
        <h1>402 Payment Required</h1>
        <p>Требуется оплата для доступа к ресурсу</p>
    </body>
</html>
""", 402

@app.route('/403')
def forbidden():
    return """
<!doctype html>
<html>
    <body>
        <h1>403 Forbidden</h1>
        <p>Доступ к ресурсу запрещен</p>
    </body>
</html>
""", 403

@app.route('/405')
def method_not_allowed():
    return """
<!doctype html>
<html>
    <body>
        <h1>405 Method Not Allowed</h1>
        <p>Метод запроса не поддерживается для данного ресурса</p>
    </body>
</html>
""", 405

@app.route('/418')
def teapot():
    return """
<!doctype html>
<html>
    <body>
        <h1>418 I'm a teapot</h1>
        <p>Я чайник и не могу заваривать кофе</p>
    </body>
</html>
""", 418
@app.route('/server_error')
def server_error_test():
    result = 10 / 0
    return "Этот код никогда не выполнится"

@app.errorhandler(500)
def internal_server_error(err):
    return """
<!doctype html>
<html>
    <body>
        <h1>Ошибка сервера</h1>
        <p>На сервере произошла внутренняя ошибка. Наши инженеры уже работают над решением проблемы.</p>
        <p>Попробуйте обновить страницу через несколько минут или вернуться на <a href="/">главную страницу</a>.</p>
        <details>
            <summary>Техническая информация (для администратора)</summary>
            <p><strong>Тип ошибки:</strong> Internal Server Error</p>
            <p><strong>Описание:</strong> Произошла непредвиденная ошибка при обработке запроса</p>
        </details>
        <p>Если проблема повторяется, пожалуйста, свяжитесь с технической поддержкой.</p>
    </body>
</html>
""", 500