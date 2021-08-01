import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype='uint8')
cv2.rectangle(img, (0,0), (500,150), (123,200,98), 3, lineType=8, shift=8)


cv2.imshow('dark', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



print(img)


