from PIL import Image
from flask import Flask, request, Response
import json
from recognizer import Recognizer
import numpy as np

app = Flask(__name__)
recognizer=Recognizer("models/yolov5n.pt")

def default(o):
  if isinstance(o, np.float32):
      return float(o)
  raise TypeError


@app.route('/image', methods=['POST'])
def process_image():
  file = request.files['image']
  image = Image.open(file.stream)    # Open the image file

  annot_list=recognizer.recognize(image)
  json_str= json.dumps(annot_list, default=default)
  return Response(response=json_str, status=200, mimetype="application/json")


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8888)
  