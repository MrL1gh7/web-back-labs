from flask import Blueprint, render_template, request, redirect, url_for, abort

lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слэша'
@lab2.route("/lab2/a/")
def a2():
    return 'со слэшем'
flower_list = [
    {'name': 'роза', 'price': 120},
    {'name': 'тюльпан', 'price': 90},
    {'name': 'незабудка', 'price': 60},
    {'name': 'ромашка', 'price': 50}
]

@lab2.route('/lab2/flowers_list')
def show_flowers():
    return render_template('flowers.html', flowers=flower_list)

@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list) or flower_id < 0:
        abort(404)
    flower = flower_list[flower_id]
    return render_template('flower.html', flower=flower, flower_id=flower_id)

@lab2.route('/lab2/flowers/add', methods=['POST'])
def add_flower_post():
    name = request.form['name']
    price = int(request.form['price'])
    flower_list.append({'name': name, 'price': price})
    return redirect(url_for('lab2.show_flowers')) 

@lab2.route('/lab2/flowers/delete/<int:flower_id>')
def delete_flower(flower_id):
    if flower_id >= len(flower_list) or flower_id < 0:
        abort(404)
    deleted = flower_list.pop(flower_id)
    return redirect(url_for('lab2.show_flowers'))

@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('lab2.show_flowers'))
@lab2.route('/lab2/example')
def example():
    name = 'Окачутин Вячеслав'
    nomer = '2'
    group = 'ФБИ-33'
    kurs = '3 курс'
    lab_num = '2'
    fruits = [{'name': 'яблоки', 'price': 100}, 
              {'name': 'груши', 'price': 100}, 
              {'name': 'апельсины' , 'price': 100},
              {'name': 'мандарины', 'price': 100}, 
              {'name': 'манго', 'price': 100},]
    return render_template('example.html', name=name, nomer=nomer, kurs=kurs, group=group, lab_num=lab_num, fruits=fruits)
@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')
@lab2.route('/lab2/filters')
def filters():
    phrase = "0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filters.html', phrase=phrase)

@lab2.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')

@lab2.route('/lab2/calc/<int:a>')
def calc_one_arg(a):
    return redirect(f'/lab2/calc/{a}/1')

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    if b == 0:
        div_result = "Ошибка: деление на ноль"
    else:
        div_result = a / b

    return f'''
<!doctype html>
<html>
    <body>
        <h1>Калькулятор</h1>
        <p>Первое число: {a}</p>
        <p>Второе число: {b}</p>
        <ul>
            <li>Сумма: {a + b}</li>
            <li>Разность: {a - b}</li>
            <li>Произведение: {a * b}</li>
            <li>Деление: {div_result}</li>
            <li>Возведение в степень: {a ** b}</li>
        </ul>
        <p><a href="/lab2/calc/">Попробовать снова с 1 и 1</a></p>
    </body>
</html>
'''
books = [
    {"author": "Дж. К. Роулинг", "title": "Гарри Поттер и философский камень", "genre": "Фэнтези", "pages": 432},
    {"author": "Дж. Р. Р. Толкин", "title": "Властелин колец: Братство кольца", "genre": "Фэнтези", "pages": 576},
    {"author": "Артур Конан Дойл", "title": "Собака Баскервилей", "genre": "Детектив", "pages": 320},
    {"author": "Дэн Браун", "title": "Код да Винчи", "genre": "Триллер", "pages": 480},
    {"author": "Джордж Мартин", "title": "Игра престолов", "genre": "Фэнтези", "pages": 864},
    {"author": "Агата Кристи", "title": "Убийство в Восточном экспрессе", "genre": "Детектив", "pages": 288},
    {"author": "Рэй Брэдбери", "title": "Марсианские хроники", "genre": "Фантастика", "pages": 352},
    {"author": "Стивен Кинг", "title": "Зелёная миля", "genre": "Драма", "pages": 544},
    {"author": "Эрих Мария Ремарк", "title": "Три товарища", "genre": "Роман", "pages": 480},
    {"author": "Антуан де Сент-Экзюпери", "title": "Маленький принц", "genre": "Сказка", "pages": 112}
]

@lab2.route('/lab2/books')
def show_books():
    lab_num = '2'
    return render_template('books.html', books=books, lab_num=lab_num)

cars = [
    {"name": "Tesla Model S", "image": "lab2/tesla_model_s.jpg", "description": "Электрический седан с мощным ускорением и автопилотом."},
    {"name": "BMW M5", "image": "lab2/bmw_m5.jpg", "description": "Спортивный седан бизнес-класса с мощным V8 двигателем."},
    {"name": "Mercedes-Benz G-Class", "image": "lab2/mercedes_g_class.jpg", "description": "Легендарный внедорожник с премиальным интерьером."},
    {"name": "Audi R8", "image": "lab2/audi_r8.jpg", "description": "Суперкар с двигателем V10 и фирменным полным приводом Quattro."},
    {"name": "Toyota Supra", "image": "lab2/toyota_supra.jpg", "description": "Японский спорткар с турбированным двигателем и культовым дизайном."},
    {"name": "Ford Mustang", "image": "lab2/ford_mustang.jpg", "description": "Американская классика — мускулистый купе с громким ревом двигателя."},
    {"name": "Lamborghini Aventador", "image": "lab2/lamborghini_aventador.jpg", "description": "Итальянский суперкар с атмосферным V12 и футуристичным дизайном."},
    {"name": "Porsche 911", "image": "lab2/porsche_911.jpg", "description": "Легендарное купе с идеальной управляемостью и мощным оппозитным мотором."},
    {"name": "Nissan GT-R", "image": "lab2/nissan_gtr.jpg", "description": "Суперкар, прозванный 'Godzilla', благодаря мощи и технологиям."},
    {"name": "Chevrolet Camaro", "image": "lab2/chevrolet_camaro.jpg", "description": "Мускул-кар с агрессивным дизайном и громким характером."},
]
@lab2.route("/lab2/cars")
def show_cars():
    lab_num = '2'
    return render_template("cars.html", cars=cars, lab_num=lab_num)