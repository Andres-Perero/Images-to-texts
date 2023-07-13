from flask import Flask, render_template, request
import pytesseract
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    uploaded_files = request.files.getlist('file')
    extracted_text = []
    
    for file in uploaded_files:
        img = cv2.imdecode(
            np.fromstring(file.read(), np.uint8), 
            cv2.IMREAD_COLOR
        )
        text = pytesseract.image_to_string(img)
        extracted_text.append(text)

    return render_template('result.html', extracted_text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)
