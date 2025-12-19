from flask import Blueprint, render_template, request, jsonify

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def lab():
    return render_template('lab7/index.html')

films = [
    {
        "title": "Astérix le Gaulois",
        "title_ru": "Астерикс — галл",
        "year": 1967,
        "description": "Первый мультфильм об Астериксе. Римляне хотят захватить деревню галлов, но Астерикс и Обеликс с помощью волшебного зелья друида противостоят им."
    },
    {
        "title": "Astérix et Cléopâtre",
        "title_ru": "Астерикс и Клеопатра",
        "year": 1968,
        "description": "Астерикс и Обеликс отправляются в Египет, чтобы помочь архитектору Нумеробису построить дворец для Клеопатры за три месяца."
    },
    {
        "title": "Les Douze Travaux d'Astérix",
        "title_ru": "12 подвигов Астерикса",
        "year": 1976,
        "description": "Римляне бросают вызов Астериксу и Обеликсу — выполнить 12 подвигов, подобных подвигам Геракла, чтобы доказать, что они боги."
    },
    {
        "title": "Astérix et la Surprise de César",
        "title_ru": "Астерикс и сюрприз Цезаря",
        "year": 1985,
        "description": "Подруга Астерикса Фальбала похищена римлянами, и герои отправляются на ее спасение в римский лагерь."
    },
    {
        "title": "Astérix chez les Bretons",
        "title_ru": "Астерикс в Британии",
        "year": 1986,
        "description": "Астерикс и Обеликс отправляются в Британию, чтобы помочь своему кузену Антиклимаксу противостоять римским завоевателям."
    },
    {
        "title": "Astérix et le Coup du menhir",
        "title_ru": "Астерикс и удар менгира",
        "year": 1989,
        "description": "После удара менгира по голове друид Панорамикс теряет память и не может готовить волшебное зелье, что ставит деревню под угрозу."
    },
    {
        "title": "Astérix et les Indiens",
        "title_ru": "Астерикс и индейцы",
        "year": 1994,
        "description": "Астерикс и Обеликс путешествуют в Америку, где встречают индейцев и помогают им противостоять коварным конкистадорам."
    },
    {
        "title": "Astérix et les Vikings",
        "title_ru": "Астерикс и викинги",
        "year": 2006,
        "description": "Викинги похищают племянника вождя, и Астерикс с Обеликсом отправляются в Скандинавию, чтобы спасти его."
    },
    {
        "title": "Astérix : Le Domaine des dieux",
        "title_ru": "Астерикс: Земля богов",
        "year": 2014,
        "description": "Юлий Цезарь решает построить римский жилой комплекс рядом с деревней галлов, чтобы ассимилировать их римской культурой."
    },
    {
        "title": "Astérix : Le Secret de la potion magique",
        "title_ru": "Астерикс: Тайное зелье",
        "year": 2018,
        "description": "Когда заканчивается волшебное зелье, Астерикс и Обеликс отправляются на поиски нового друида, который сможет приготовить его."
    },
    {
        "title": "Astérix et Obélix : Mission Cléopâtre",
        "title_ru": "Астерикс и Обеликс: Миссия Клеопатра",
        "year": 2002,
        "description": "Игровой фильм с Жераром Депардье и Кристианом Клавье. Герои помогают построить дворец для Клеопатры за три месяца."
    },
    {
        "title": "Astérix aux Jeux Olympiques",
        "title_ru": "Астерикс на Олимпийских играх",
        "year": 2008,
        "description": "Астерикс и Обеликс участвуют в Олимпийских играх, чтобы помочь своему другу выиграть соревнования и жениться на принцессе."
    },
    {
        "title": "Astérix et Obélix : Au service de Sa Majesté",
        "title_ru": "Астерикс и Обеликс на службе Её Величества",
        "year": 2012,
        "description": "Герои отправляются в Британию, чтобы помочь королеве противостоять римлянам и найти пропавшего шпиона."
    }
]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        return '', 404
    return films[id]

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        return '', 404
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    film = request.get_json()
    
    # Если оригинальное название пустое, а русское задано - используем русское
    if (not film.get('title') or film['title'].strip() == '') and film.get('title_ru'):
        film['title'] = film['title_ru']
    
    # Проверка обязательных полей
    required_fields = ['title_ru', 'year', 'description']
    for field in required_fields:
        if field not in film or not str(film[field]).strip():
            return {field: 'Это поле обязательно для заполнения'}, 400
    
    # Проверка на существующий ID
    if id < 0 or id >= len(films):
        return '', 404
    
    films[id] = film
    return films[id]

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    data = request.get_json()
    
    if not data:
        return '', 400
    
    # Если оригинальное название пустое, а русское задано - используем русское
    if (not data.get('title') or data['title'].strip() == '') and data.get('title_ru'):
        data['title'] = data['title_ru']
    
    # Проверка обязательных полей
    required_fields = ['title_ru', 'year', 'description']
    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return {field: 'Это поле обязательно для заполнения'}, 400
    
    # Проверка года (должен быть числом)
    try:
        year = int(data['year'])
        if year < 1888 or year > 2100:
            return {'year': 'Некорректный год выпуска'}, 400
    except ValueError:
        return {'year': 'Год должен быть числом'}, 400
    
    new_film = {
        'title': data.get('title', ''),
        'title_ru': data['title_ru'],
        'year': year,
        'description': data['description']
    }
    
    films.append(new_film)
    return str(len(films) - 1), 201