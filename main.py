import cv2
import matplotlib.pyplot as plt
import numpy as np
import imutils 
import easyocr
import os

def read_text(filename):
    print("Starting filename:", filename)
    img = cv2.imread(filename)
    # print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray)
    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    bfilter = cv2.bilateralFilter(gray, 11, 11, 17)
    edged = cv2.Canny(bfilter, 30, 200)
    plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
    #  cv.CHAIN_APPROX_NONE gives (734 points) and  with cv.CHAIN_APPROX_SIMPLE (only 4 points)

    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Simplifies how contonours are actually returned
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
    # print(contours)

    location = None

    for contour in contours:
    # cv2.approxPolyDP returns a resampled contour, so this will still return a set of (x, y) points
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break

    # print(location)
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)

    new_image = cv2.bitwise_and(img, img, mask = mask)


    plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    (x, y) = np.where(mask == 255)

    (x1, y1) = (np.min(x), np.min(y))

    (x2, y2) = (np.max(x), np.max(y))

    cropped_image = gray[x1:x2+3, y1:y2+3]

    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))

    reader = easyocr.Reader(['en'])

    result = reader.readtext(cropped_image)

    # print(result)
    # print(result[0][0])
    # print(result[0][1])
    text = result[0][1]

    font = cv2.FONT_HERSHEY_SIMPLEX
    res = cv2.putText(img, text = text, org = (approx[0][0][0], approx[1][0][1]+60), fontFace = font, fontScale = 1, color = (0, 255, 0), thickness = 5)
    res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255, 0), 3)

    res = plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
    # s = plt.imsave("op.png", cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
    # print(res)
    print("Filename:", filename,", Text:", text)


files = os.listdir('.\\train')

for file in files:
    try:
        read_text('.\\train\\' + file)
    except:
        print("Could not read file")