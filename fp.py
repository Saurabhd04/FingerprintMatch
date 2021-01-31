import cv2
import numpy as np
import matplotlib.pyplot as plt

def isMatch(fImage, DbImage):
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints_1, descriptors_1 = sift.detectAndCompute(fImage, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(DbImage, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(descriptors_1,descriptors_2, k=2)

    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
    goodMatches = len(good)
    print(goodMatches)
    
    if goodMatches > 50:
        return True
    return False
    # img3 = cv2.drawMatchesKnn(fImage,keypoints_1,DbImage,keypoints_2,good,None,flags=2)
    # plt.imshow(img3),plt.show()

# if __name__ == "__main__":
    
#     fImage = cv2.imread("C:/Program Files/Mantra/MFS100/Driver/MFS100Test/FingerData/FingerImage.bmp")

#     # cv2.imshow("original",cv2.resize(fImage, None, fx=1, fy=1))
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
#     DbImage = cv2.imread("C:/Users/Sourabh/FingerImage.bmp")

#     isMatch(fImage, DbImage)

