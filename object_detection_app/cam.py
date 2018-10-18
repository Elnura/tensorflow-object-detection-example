import urllib3
import cv2
import numpy as np
from io import StringIO
from PIL import Image
import io

class ipCamera:
    def __init__(self, url, user=None, password=None):
        self.url = url
        try:
            http = urllib3.PoolManager()
            headers = urllib3.util.make_headers(basic_auth='{}:{}'.format(user, password))
            http.headers = headers
            self.http = http
        except:
            print('Error occurred:') # log error message with time occured

    def get_frame(self):
        try:
            r = self.http.request('GET', self.url)
            resized_image = Image.open(io.BytesIO(r.data))
            frame = np.array(resized_image)
            return frame
        except:
           return None # change it to an empty object of image

#url = 'http://172.21.2.254/fastjpeg?stamp=0.383161508780318.jpg'
#page = requests.get(url)
#soup = BeautifulSoup(page.text, 'html.parser')
#src = soup.find_all(id='img_sub_datetime_activex_tmp') ### src kaynağını al

