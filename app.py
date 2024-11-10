from flask import Flask, render_template, request, jsonify
import alexa  # Import your Alexa code file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_command', methods=['POST'])
def process_command():
    command = request.json.get('command')
    # Run the command in your Alexa app
    response = alexa.run_command(command)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
