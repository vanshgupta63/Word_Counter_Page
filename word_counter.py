# word_counter.py
from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Function to count words in a file
def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            words = text.split()
            return len(words), None
        
    except FileNotFoundError:
        return 0, "File not found."
    except Exception as e:
        return 0, str(e)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            file_path = os.path.join('uploads', file.filename)
            os.makedirs('uploads', exist_ok=True)
            file.save(file_path)
            word_count, error = count_words(file_path)
            return render_template('result.html', word_count=word_count, error=error, filename=file.filename)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
