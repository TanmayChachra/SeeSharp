from flask import Flask, url_for, render_template, request
import multifacerecognition as mfr
from PIL import Image
import PIL

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/response',methods=['POST','GET'])
# def recogniseFace():
#     if request.method == 'POST':
#         image = request.form['image']
#         print(type(image))
#         # mfr.run(image)
#         return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)