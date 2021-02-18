
# https://medium.com/@tasnuva2606/dockerize-flask-app-4998a378a6aa
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
