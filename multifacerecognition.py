import face_recognition as fr
import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import base64

def encode_faces(folder):
        list_people_encoding = []
        for filename in os.listdir(folder):
            known_image = fr.load_image_file(f'{folder}/{filename}')
            known_encoding = fr.face_encodings(known_image)[0]
            list_people_encoding.append((known_encoding, filename))
        return list_people_encoding

def find_target_face():
    face_location = fr.face_locations(target_image)
    for person in encode_faces('photos'):
        encoded_face = person[0]
        filename = person[1]
        is_target_face = fr.compare_faces(encoded_face, target_encoding, tolerance=0.55)
        print(f'{filename} is {is_target_face}')
        
        if face_location:
            face_number = 0
            for location in face_location:
                if is_target_face[face_number]:
                    label = filename
                    create_frame(location, label)
                face_number+=1
def create_frame(location, label):
    top,right,bottom,left=location

    cv.rectangle(target_image, (left, top), (right, bottom), (255,0,0), 2)
    cv.rectangle(target_image, (left, bottom +20), (right, bottom), (255,0,0), cv.FILLED)
    cv.putText(target_image, label, (left+3, bottom+14), cv.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 1)

def render_image():
    rgb_img = cv.cvtColor(target_image, cv.COLOR_BGR2RGB)
    cv.imshow('Face Recognition', rgb_img)
    cv.waitKey(0)

def run(image):
    global target_image, target_encoding
    # Tk().withdraw
    # load_image = askopenfilename()
    img = base64.b64decode(image)
    target_image = fr.load_image_file(img)
    target_encoding = fr.face_encodings(target_image)
    # print(target_encoding)

    find_target_face()
    render_image()

if __name__ == "__main__":
    run()


