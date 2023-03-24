from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    return "Главная страничка"

@app.route("/feed")
def page_feed():
        return "Лента новостей"

@app.route("/messages")
def page_messages():
    return "Сообщения пользователя"

@app.route('/users/<uid>')
def page_profile(uid):
    return f'<h1>Профиль {uid}</h1>'

@app.route('/catalog/items/<itemid>')
def profile(itemid):
    return f'<h1>Страничка товара {itemid}</h1>'

app.run(host='127.0.0.21', port='80', debug=True)

hahah
