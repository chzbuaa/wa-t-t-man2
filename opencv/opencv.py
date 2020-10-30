import cv2
from boxtool import re

x1 = re['right_bottom'][0]
x2 = re['left_top'][0]
y1 = re ['right_bottom'][1]
y2 = re['left_top'][1]
x = x1 - x2
y = y1 - y2



# Load two images
img1 = cv2.imread('messi5.jpg')  # 背景图片
img2 = cv2.imread('opencv-logo-white.png')  # 填充图片


# img_2 = cv2.resize(img2,(int(x),int(y)))
img2 = cv2.resize(img2,(x,y),interpolation=cv2.INTER_AREA)
# img2 = cv2.resize(img2,(0,0),fx = 2,fy = 2)
print(img1.shape)
print(img2.shape)


# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[x2:rows+x2, y2:cols+y2]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)


# img1[x2:x2+x, y2:y2+y] = dst
img1[x2:rows+x2, y2:cols+y2] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
