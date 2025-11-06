from flask import Flask, url_for, request, redirect, abort, render_template
import datetime
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
app = Flask(__name__)
app.secret_key = 'Секретно-секретный ключ'
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)

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
                    <li><a href='/lab2'>Вторая лабораторная</a></li>
                    <li><a href='/lab3'>Третья лабораторная</a></li>
                    <li><a href='/lab4'>Четвертая лабораторная</a></li>
                </ul>
                <footer>
                    Окачутин Вячеслав Владимирович, ФБИ-33, 3 курс, 2025
                </footer>
            </body>
        </html>'''

error_404_log = []

@app.errorhandler(404)
def not_found(err):

    client_ip = request.remote_addr
    access_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    requested_url = request.url
    user_agent = request.headers.get('User-Agent', 'Неизвестно')
    
    log_entry = {
        'ip': client_ip,
        'time': access_time,
        'url': requested_url,
        'user_agent': user_agent
    }
    error_404_log.append(log_entry)
    
    css_path = url_for("static", filename="error.css")
    image_path = url_for("static", filename="404.jpg")
    
    
    log_html = ""
    for entry in reversed(error_404_log[-10:]):
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
