from flask import Blueprint, render_template, request, make_response, redirect

lab3 = Blueprint('lab3', __name__)

@lab3.route("/lab3/")
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color)
@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp
@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp
@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните имя!'
    er_age = {}
    age = request.args.get('age')
    if age == '':
        er_age['age'] = 'Заполните возраст!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors, er_age=er_age)
@lab3.route('/lab3/order')
def order():
    return render_template('/lab3/order.html')
@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('lab3/pay.html', price=price)
@lab3.route('/lab3/payment')
def payment():
    price = request.args.get('price')
    return render_template('lab3/payment.html', price=price)
@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    if color or bg_color or font_size:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if bg_color:
            resp.set_cookie('bg_color', bg_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        return resp
    color = request.cookies.get('color', '#000000')
    bg_color = request.cookies.get('bg_color', '#ffffff')
    font_size = request.cookies.get('font_size', '16')
    
    return render_template('lab3/settings.html', 
                         color=color, 
                         bg_color=bg_color, 
                         font_size=font_size)
@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    
    fio = request.args.get('fio')
    shelf = request.args.get('shelf')
    linen = request.args.get('linen') == 'on'
    luggage = request.args.get('luggage') == 'on'
    age_str = request.args.get('age')
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    travel_date = request.args.get('travel_date')
    insurance = request.args.get('insurance') == 'on'
    
    form_submitted = any([fio, shelf, age_str, departure, destination, travel_date])
    
    if form_submitted:
        if not fio:
            errors['fio'] = 'Заполните ФИО пассажира'
        if not shelf:
            errors['shelf'] = 'Выберите полку'
        if not age_str:
            errors['age'] = 'Заполните возраст'
        elif not age_str.isdigit() or not (1 <= int(age_str) <= 120):
            errors['age'] = 'Возраст должен быть от 1 до 120 лет'
        if not departure:
            errors['departure'] = 'Заполните пункт выезда'
        if not destination:
            errors['destination'] = 'Заполните пункт назначения'
        if not travel_date:
            errors['travel_date'] = 'Выберите дату поездки'
        
        if errors:
            return render_template('lab3/ticket.html', 
                                 errors=errors,
                                 fio=fio,
                                 shelf=shelf,
                                 linen=linen,
                                 luggage=luggage,
                                 age=age_str,
                                 departure=departure,
                                 destination=destination,
                                 travel_date=travel_date,
                                 insurance=insurance,
                                 show_result=False)
        
        age = int(age_str)
        if age < 18:
            price = 700
        else:
            price = 1000
        
        if shelf in ['lower', 'side_lower']:
            price += 100
        if linen:
            price += 75
        if luggage:
            price += 250
        if insurance:
            price += 150
        
        return render_template('lab3/ticket.html',
                             fio=fio,
                             shelf=shelf,
                             linen=linen,
                             luggage=luggage,
                             age=age,
                             departure=departure,
                             destination=destination,
                             travel_date=travel_date,
                             insurance=insurance,
                             price=price,
                             show_result=True)
    
    return render_template('lab3/ticket.html', show_result=False)
@lab3.route('/lab3/clear_settings')
def clear_settings():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('bg_color') 
    resp.delete_cookie('font_size')
    return resp