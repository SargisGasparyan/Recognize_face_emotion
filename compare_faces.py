import face_recognition

def compare(image1, image2):
    unknown_image1 = face_recognition.load_image_file(image1)
    unknown_image2 = face_recognition.load_image_file(image2)

    try:
        unknown_face_encoding1 = face_recognition.face_encodings(unknown_image1)[0]
        unknown_face_encoding2 = face_recognition.face_encodings(unknown_image2)[0]
    except IndexError:
        return "not face"

    known_faces = [
        unknown_face_encoding1
    ]
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding2)

    return str(results[0])