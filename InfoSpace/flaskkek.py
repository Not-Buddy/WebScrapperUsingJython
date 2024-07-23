
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    return f'Search results for: {query}'

if __name__ == '__main__':
    app.run(debug=True)

