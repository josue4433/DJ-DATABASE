from Flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    return 'Welcome to my playlist app!'