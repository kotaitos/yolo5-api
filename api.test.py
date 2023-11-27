# 0.0.0.0:8888にtest.jpgをPOSTするテストを記述する。
#
# Path: api.test.py
import requests

def test_api():
  url = "http://0.0.0.0:8888/image"
  files = {'image': open('test.jpg', 'rb')}
  response = requests.post(url, files=files)
  print(response.status_code)
  print(response.text)


if __name__ == "__main__":
  test_api()
  print('done')
  