from flask import Flask, render_template
import pullData
app = Flask(__name__)


@app.route('/')
def renderHome():
    return render_template('index.html')

@app.route('/tacos')
def renderTacoList():
  return render_template('tacoList.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')