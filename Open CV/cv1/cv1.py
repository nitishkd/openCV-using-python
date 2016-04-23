import cv2
import numpy as np
import matplotlib.pyplot as plt

##read image and chage it into grayscale
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
#other functions
#IMREAD_COLOR - 1
#IMREAD_UNCHANGED = -1

#-----------------------------------
##show image using opencv
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-----------------------------------
#to write an image with other name
cv2.imwrite('watchgray.png', img)



#_------------------------------------
#show image using matplotlib


plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.plot([50,100],[80,100], 'c',linewidth=5)
plt.show()


