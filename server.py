from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World!'


@app.route('/play')
def play():
    return render_template('index.html', num=3, color='blue')

@app.route('/play/<num>')

def play_count(num):
    num = int(num)
    return render_template('index.html', num=num, color='blue')


@app.route('/play/<num>/<color>')
def play_count_color(num, color):
    num = int(num)
    return render_template('index.html', num=num, color=color)










if __name__=="__main__":
    app.run(debug=True)