from flask import Flask, url_for, request, redirect, abort, render_template
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
                <li><a href="''' + url_for('created') + '''">Создано успешно</a></li>
                <li><a href="''' + url_for('bad_request') + '''">400</a></li>
                <li><a href="''' + url_for('unauthorized') + '''">401</a></li>
                <li><a href="''' + url_for('payment_required') + '''">402</a></li>
                <li><a href="''' + url_for('forbidden') + '''">403</a></li>
                <li><a href="''' + url_for('method_not_allowed') + '''">405</a></li>
                <li><a href="''' + url_for('teapot') + '''">418</a></li>
                <li><a href="''' + url_for('server_error_test') + '''">500</a></li>
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
                <a href=""" + url_for('web') + """>web</a>
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
    </html>""", 200, {
        'Content-Language': 'ru',
        'X-Developer': 'Okachuchin Vyacheslav',
        'X-App-Version': '1.0',
        'X-Custom-Header': 'Flask-Lab-Work'
    }

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
    return redirect(url_for('author'))

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

# Глобальный список для хранения лога 404 ошибок
error_404_log = []

@app.errorhandler(404)
def not_found(err):
    # Получаем данные о запросе
    client_ip = request.remote_addr
    access_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    requested_url = request.url
    user_agent = request.headers.get('User-Agent', 'Неизвестно')
    
    # Добавляем запись в лог
    log_entry = {
        'ip': client_ip,
        'time': access_time,
        'url': requested_url,
        'user_agent': user_agent
    }
    error_404_log.append(log_entry)
    
    css_path = url_for("static", filename="error.css")
    image_path = url_for("static", filename="404.jpg")
    
    # Формируем HTML с логом
    log_html = ""
    for entry in reversed(error_404_log[-10:]):  # Последние 10 записей
        log_html += f"""
        <div class="log-entry">
            <strong>Время:</strong> {entry['time']} | 
            <strong>IP:</strong> {entry['ip']} | 
            <strong>URL:</strong> {entry['url']} | 
            <strong>Браузер:</strong> {entry['user_agent'][:50]}...
        </div>
        """
    
    return f"""
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
        <title>Страница не найдена</title>
        <style>
            .log-entry {{
                background: rgba(255,255,255,0.1);
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
                font-family: monospace;
                font-size: 0.9em;
            }}
            .info-block {{
                background: rgba(255,255,255,0.1);
                padding: 15px;
                border-radius: 10px;
                margin: 15px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Ой! Кажется, мы потеряли эту страницу...</h1>
            <div class="error-code">404</div>
            <img src="{image_path}" alt="Потерянная страница">
            
            <div class="info-block">
                <h3>Информация о вашем запросе:</h3>
                <p><strong>Ваш IP-адрес:</strong> {client_ip}</p>
                <p><strong>Дата и время доступа:</strong> {access_time}</p>
                <p><strong>Запрошенный адрес:</strong> {requested_url}</p>
            </div>
            
            <p>Запрашиваемая страница куда-то пропала. Возможно, она переехала или никогда не существовала.</p>
            <p>Попробуйте вернуться на <a href="{url_for('index')}">главную страницу</a> или проверьте правильность адреса.</p>
            
            <div class="fun-fact">
                <strong>Интересный факт:</strong> В интернете ежедневно теряется более 1 миллиона страниц!
            </div>
            
            <div class="info-block">
                <h3>Журнал 404 ошибок (последние 10 записей):</h3>
                {log_html if log_html else "<p>Пока нет записей в журнале</p>"}
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
@app.route('/lab2/a')
def a():
    return 'без слэша'
@app.route("/lab2/a/")
def a2():
    return 'со слэшем'
flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']
@app.route('/lab2/flowers/<int:flower_id>')
def frowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return "id=" + flower_list[flower_id]
@app.route('/lab2/flowers/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен цветок</h1>
    <p>Название нового цветка: {name}</p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''
@app.route('/lab2/example')
def example():
    student = 'Окачутин Вячеслав'
    nomer = '2'
    group = 'ФБИ-33'
    course = '3 курс'
    lab_num = '2'
    return render_template('example.html', name=student, nomer=nomer, group=group, course=course, lab_num=lab_num)