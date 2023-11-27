import cv2
from ultralytics import YOLO

class Recognizer:
  def __init__(self,model_path):
    self.model = YOLO(model_path)
    self.names = self.model.names

  def recognize(self, img,conf=0.3):
    preds =self. model.predict(img,conf=conf)
    annot_list=[]
    for box in preds[0].boxes:
      label=self.names[box.cls.cpu().numpy()[0]]
      conf=box.conf.cpu().numpy()[0]
      xmin, ymin, xmax, ymax=box.xyxy.cpu().numpy()[0]
      xmin, ymin, xmax, ymax=int(xmin), int(ymin), int(xmax), int(ymax)

      d={
        "label":label,
        "conf":conf,
        "xmin":xmin,
        "ymin":ymin,
        "xmax":xmax,
        "ymax":ymax
      }

    annot_list.append(d)
    return annot_list


if __name__ == "__main__":
  print('loading model...')
  recognizer=Recognizer("models/yolov5n.pt")
  
  print('recognizing...')
  img_path="test.jpg"
  img=cv2.imread(img_path)
  annot_list=recognizer.recognize(img)
  print(annot_list)
  cv2.imshow("img",img)
  cv2.waitKey(0) # press any key to exit
  cv2.destroyAllWindows()