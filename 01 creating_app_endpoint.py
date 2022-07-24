from flask import Flask,jsonify

app = Flask(__name__)

Friends = [
    {
    'name' : 'Shubh Kumar',
    'hobbies': 'music'
    },
    {
        'name' : 'Sandeep Singh',
        'hobbies' : 'Game'
    }
]

@app.route('/')
def home():
    return "This is home page"

@app.route('/friends')
def get_friends():
    return jsonify({'Friends': Friends})

app.run(port=8000)
