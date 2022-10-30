import numpy as np
from PIL import Image

#create  3d numpy array of zeros (black pixels with yellow pxls
data = np.zeros((5,4,3), dtype=np.uint8)
data[:] = [255,255,0]
print(data)
#make a red path
data[0:5,0:3] = [150,230,15]
data[3:4,1:2] = [255,30,15]

img  = Image.fromarray(data, 'RGB')
img.save('canvas.png')