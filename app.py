from flask import Flask, render_template, request, jsonify
from Sorting import sort_array
from Chatbot import get_chatbot_response
from Digital_twin import analyze_behavior

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    data = request.get_json()
    array = data['array']
    algorithm = data['algorithm']
    result = sort_array(array, algorithm)
    feedback = analyze_behavior(result)
    return jsonify({"result": result, "feedback": feedback})

@app.route('/chat', methods=['POST'])
def chat():
    message = request.get_json()['message']
    response = get_chatbot_response(message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)