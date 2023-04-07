from flask import Flask


app = Flask(__name__)



@app.route("/link")
def page_link():
        return "<a href='www.youtube.com'>LINK</a>"


@app.route('/haha//<int:num>')
def haha(num):
    print(num)
    print(int(num))
    return f'<h1>Вы написали число {num} в URL строке</h1>'







app.run(host='127.0.0.21', port=5000)