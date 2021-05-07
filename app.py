import os
from flask import Flask, render_template, request, jsonify
from compare_faces import compare
import requests
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = ""
CORS(app)
url = 'https://crm-emotion-rec.herokuapp.com/emotion_recognizer'
image2 = 'img.jpg'

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/face_noFace', methods = ['GET', 'POST'])
@cross_origin()
def face_or_other():
   if request.method == 'POST':
       image1 = request.files['image1']
       image1.save(os.path.join(app.config["IMAGE_UPLOADS"], image1.filename))
       response = compare(image1, image2)
       if ((response == 'True') or (response == 'False') ):
           return jsonify(
               response='face')
       else:
           return jsonify(
               response='no_face')
if __name__ == '__main__':
    app.run()
