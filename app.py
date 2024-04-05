from flask import Flask, render_template, request
from chatbot import chatbot  # Import your chatbot function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        input_text = request.form['input_text']
        output_text = chatbot(input_text)
        return {'response': output_text}

if __name__ == '__main__':
    app.run(debug=True)
