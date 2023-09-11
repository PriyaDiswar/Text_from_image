!pip install easyocr

import easyocr
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/download (2).jpg")    #file path in quotes

plt.imshow(img);
plt.show()

read=easyocr.Reader(['en'])

read.readtext(img)

data=read.readtext(img)
for i in data:
  print(i[1])
  
"""Testing"""