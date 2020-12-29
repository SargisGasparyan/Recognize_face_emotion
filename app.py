import os
from flask import Flask, render_template, request, jsonify
from compare_faces import compare
import requests
import json

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = ""
port = int(os.environ.get("PORT", 7000))
url = 'https://crm-emotion-rec.herokuapp.com/emotion_recognizer'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/face_recognizer', methods = ['GET', 'POST'])
def recocnize_faces():
   if request.method == 'POST':
       image1 = request.files['image1']
       image2 = request.files['image2']
       image1.save(os.path.join(app.config["IMAGE_UPLOADS"], image1.filename))
       image2.save(os.path.join(app.config["IMAGE_UPLOADS"], image2.filename))
       response = compare(image1, image2)
       image = {'image': open(image2.filename, 'rb')}
       emotion = requests.post(url, files=image).json()
       emotion = emotion["resp_emotion"]
       if response == 'True':
           return jsonify(
               ImageProfile=image1.filename,
               ImageWebcam=image2.filename,
               Emotion=emotion,
               response=response)
       else:
           return jsonify(
               ImageProfile=image1.filename,
               ImageWebcam=image2.filename,
               response=response)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)
