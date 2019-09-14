from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'

@app.route('/bot')
def func_name():
    return render_template('bot.html')

if __name__ == '__main__':
  app.run(debug=True)
 