import easyocr
import cv2
import matplotlib.pyplot as plt
import openpyxl
import time
t1=time.time()
def point():
    while True:
        cap = cv2.VideoCapture(0)
        cap.set(3, 848)
        cap.set(4, 480)
        cap.set(28, 225)
        sucess, image = cap.read()
        t2=time.time()
        if (t2-t1)>3:
            cv2.imwrite("image1.jpg",image)
            break
    result_f={}
    cap.release()
    cv2.destroyAllWindows()
    img=cv2.imread("C:/Users/Prajwal/Python Projects/Weimar SRA/TRIALS 1/image1.jpg")
    reader = easyocr.Reader(['en'],gpu=False)
    gray = cv2.medianBlur(img,1)
    # Apply thresholding to preprocess the image
    # ret, img1 = cv2.threshold(gray, 20, 250, cv2.THRESH_BINARY_INV)
    #display(img1)  
    result = reader.readtext(img) ##img1
    #cv2.imwrite("image.png", image)

    print(img.shape)
    for i in range(len(result)):
        cv2.rectangle(img, (result[i][0][0][0], result[i][0][0][1]), (result[i][0][2][0], result[i][0][2][1]), (0, 255, 0), 2)
        cv2.putText(img,result[i][1] , (result[i][0][1][0], result[i][0][1][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        result_f[result[i][1]]=[0.5*result[i][0][0][0]+0.5*result[i][0][2][0],0.5*result[i][0][0][1]+0.5*result[i][0][2][1]]
    cv2.imwrite("image3.jpg",img)
    #cv2.imshow('detected_number',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return result_f