from flask import Blueprint, render_template, request, session

lab6 = Blueprint('lab6', __name__)

# -----------------------
#  Глобальная переменная offices (как требует задание!)
# -----------------------
offices = []
for i in range(1, 11):
    offices.append({
        "number": i,
        "tenant": "",
        "price": 900 + i * 100
    })


@lab6.route('/lab6/')
def main():
    return render_template('lab6/lab6.html')


@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data["id"]

    # --------------------------------------
    # 1. Метод info — выдаёт список офисов
    # --------------------------------------
    if data["method"] == "info":
        return {
            "jsonrpc": "2.0",
            "result": offices,
            "id": id
        }

    # Все остальные методы требуют авторизации
    login = session.get("login")
    if not login:
        return {
            "jsonrpc": "2.0",
            "error": {
                "code": 1,
                "message": "Unauthorized"
            },
            "id": id
        }

    # --------------------------------------
    # 2. Метод booking — бронь офиса
    # --------------------------------------
    if data["method"] == "booking":
        office_number = data["params"]

        for o in offices:
            if o["number"] == office_number:

                # уже занят
                if o["tenant"] != "":
                    return {
                        "jsonrpc": "2.0",
                        "error": {
                            "code": 2,
                            "message": "Already booked"
                        },
                        "id": id
                    }

                # бронируем
                o["tenant"] = login

                return {
                    "jsonrpc": "2.0",
                    "result": "success",
                    "id": id
                }

        return {
            "jsonrpc": "2.0",
            "error": {
                "code": 5,
                "message": "Office not found"
            },
            "id": id
        }

    # --------------------------------------
    # 3. Метод cancellation — снятие брони
    # --------------------------------------
    if data["method"] == "cancelation":
        office_number = data["params"]

        for o in offices:
            if o["number"] == office_number:

                if o["tenant"] == "":
                    return {
                        "jsonrpc": "2.0",
                        "error": {
                            "code": 3,
                            "message": "Office is not booked"
                        },
                        "id": id
                    }

                if o["tenant"] != login:
                    return {
                        "jsonrpc": "2.0",
                        "error": {
                            "code": 4,
                            "message": "Cannot cancel other user's booking"
                        },
                        "id": id
                    }

                # снимаем аренду
                o["tenant"] = ""

                return {
                    "jsonrpc": "2.0",
                    "result": "success",
                    "id": id
                }

        return {
            "jsonrpc": "2.0",
            "error": {
                "code": 5,
                "message": "Office not found"
            },
            "id": id
        }

    # --------------------------------------
    # Неизвестный метод
    # --------------------------------------
    return {
        "jsonrpc": "2.0",
        "error": {
            "code": -32601,
            "message": "Method not found"
        },
        "id": id
    }
