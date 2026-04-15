from flask import Flask, render_template, request
import os
import backend

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('final.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'resume' not in request.files:
        return "لم يتم العثور على ملف"
    
    file = request.files['resume']
    if file.filename == '':
        return "اسم الملف فارغ"

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # استدعاء دالة التحليل من الباك إند
        result = backend.analyze_cv(file_path) 
        return render_template('final.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)