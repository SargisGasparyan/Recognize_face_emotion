import os
from flask import Flask, render_template, request, jsonify
from compare_faces import compare
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = ""
CORS(app)
# port = int(os.environ.get("PORT", 7000))
# url = 'https://crm-emotion-rec.herokuapp.com/emotion_recognizer'
image2 = 'image1.jpeg'

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/face_recognizer', methods = ['GET', 'POST'])
# def recocnize_faces():
#    if request.method == 'POST':
#        image1 = request.files['image1']
#        image2 = request.files['image2']
#        image1.save(os.path.join(app.config["IMAGE_UPLOADS"], image1.filename))
#        image2.save(os.path.join(app.config["IMAGE_UPLOADS"], image2.filename))
#        response = compare(image1, image2)
#        image = {'image': open(image2.filename, 'rb')}
#        emotion = requests.post(url, files=image).json()
#        emotion = emotion["resp_emotion"]
#        if response == 'True':
#            return jsonify(
#                ImageProfile=image1.filename,
#                ImageWebcam=image2.filename,
#                Emotion=emotion,
#                response=response)
#        else:
#            return jsonify(
#                ImageProfile=image1.filename,
#                ImageWebcam=image2.filename,
#                response=response)

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
