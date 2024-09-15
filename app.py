from flask import Flask, render_template, request, jsonify
from core1 import process_youtube_video  # Replace 'your_module' with the actual module name

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_video():
    youtube_url = request.form['youtube_url']
    results = process_youtube_video(youtube_url)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
