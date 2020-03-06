from flask import Flask, render_template
from bs0104.naver_corona import naverCorona
app = Flask(__name__)


@app.route('/')
def index():
    result  = naverCorona()
    return render_template('index.html', result = result)


@app.route('/info')
def info():
    return render_template('info.html')

#
if __name__ == '__main__':
    app.run()